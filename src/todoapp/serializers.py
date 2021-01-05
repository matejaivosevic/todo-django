from rest_framework import serializers

from src.todoapp.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name'
        )


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'password',
            'first_name',
            'last_name',
            'email'
        )