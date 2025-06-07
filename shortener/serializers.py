from rest_framework import serializers

from .models import ShortURL


class ShortURLSerializer(serializers.ModelSerializer):

    short_url = serializers.SerializerMethodField(read_only=True)
    short_code = serializers.CharField(read_only=True)
    is_expired = serializers.ReadOnlyField()

    class Meta:
        model = ShortURL
        fields = [
            'id',
            'original_link',
            'short_url',
            'short_code',
            'created_at',
            'is_active',
            'is_expired',
            'clicks',
        ]
        read_only_fields = ['id', 'short_url', 'created_at', 'clicks']

    def get_short_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f"/{obj.short_code}/")
        return f"/{obj.short_code}/"
