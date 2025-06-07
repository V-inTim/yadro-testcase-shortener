from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect

from .models import ShortURL
from .serializers import ShortURLSerializer
from .utils import generate_short_code
from .paginations import ShortURLPagination


class CreateShortURLView(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        short_code = generate_short_code()
        serializer.save(user=self.request.user, short_code=short_code)


class RedirectShortURLView(APIView):
    def get(self, request, short_code):
        url = get_object_or_404(ShortURL, short_code=short_code)
        if not url.is_active or url.is_expired:
            return Response(
                {'detail': 'Link expired or inactive'},
                status=status.HTTP_403_FORBIDDEN,
            )
        url.clicks += 1
        url.save()
        return redirect(url.original_link)


class ListShortURLsView(generics.ListAPIView):
    serializer_class = ShortURLSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ShortURLPagination

    def get_queryset(self):
        qs = ShortURL.objects.filter(user=self.request.user)
        is_active = self.request.query_params.get('is_active')
        if is_active is not None and is_active.lower() == "true":
            qs = qs.filter(is_active=True)

        ordering = self.request.query_params.get('ordering')
        if ordering is not None and ordering == "clicks":
            qs = qs.order_by('-clicks')
        return qs


class DeactivateShortURLView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, short_code):
        url = get_object_or_404(
            ShortURL,
            short_code=short_code,
            user=request.user,
        )
        if not url.is_active:
            return Response(
                {'detail': 'Link is already deactivated'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        url.is_active = False
        url.save()
        return Response(
            {'message': 'Link deactivated successfully'},
            status=status.HTTP_200_OK,
        )
