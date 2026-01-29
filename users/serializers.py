from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['is_active', ] # чтобы не мог поменять себе активность


class ClassModerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "id")
