from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import UserTagPreference

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')


class UserTagPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTagPreference
        fields = '__all__'
