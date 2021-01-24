from rest_framework import serializers
from accounts.models import CustomUser
from .models import CustomNotification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("password",)


class NotificationSerializer(serializers.ModelSerializer):
    actor = UserSerializer(read_only=True)

    class Meta:
        model = CustomNotification
        fields = "__all__"
