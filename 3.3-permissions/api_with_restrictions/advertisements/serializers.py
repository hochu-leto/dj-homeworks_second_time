from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        limit = 10
        if self.context['request'].method == 'PATCH' and data['status'] == 'CLOSED':
            return data

        opens = Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN').count()
        if opens > limit - 1:
            raise serializers.ValidationError(f'Открытых объявлений не должно быть больше {limit} '
                                              f'У вас сейчас {opens} открытых объявлений')
        return data
