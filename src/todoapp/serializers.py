from rest_framework import serializers

from src.todoapp.models import User, Item

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
        user = User.objects.create(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'password',
            'first_name',
            'last_name',
            'email'
        )

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = (
            'title',
            'description',
            'completed',
            'priority',
            'user_id'
        )

class CreateItemSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        item = Item.objects.create(**validated_data)
        return item
    
    class Meta:
        model = Item
        fields = (
            'title',
            'description',
            'completed',
            'priority',
            'user_id'
        )