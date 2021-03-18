from rest_framework import serializers
from .models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'about',
        ]


class UserDetailsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
