from django.urls import path

from .views import (
    CreateShortURLView,
    ListShortURLsView,
    DeactivateShortURLView,
    RedirectShortURLView,
)

urlpatterns = [
    path('api/shorten/', CreateShortURLView.as_view()),
    path('api/list/', ListShortURLsView.as_view()),
    path('api/deactivate/<str:short_code>/', DeactivateShortURLView.as_view()),
    path('<str:short_code>/', RedirectShortURLView.as_view()),
]
