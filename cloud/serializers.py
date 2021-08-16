from rest_framework import serializers
from django.contrib.auth.models import User
from .models import item

# User Serializer

# this is the serializer used for manging data between database and front side in JSON


class itemSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = item
        fields = ('__all__')

# this is the user serializer to manage USER functionalities


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer

# this is the user serializer to register user and token mangement


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user
