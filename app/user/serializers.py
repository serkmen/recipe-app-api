"""
Serializers for the user API view.
"""
from django.contrib.auth import get_user_model
# Converst JSON file to Python object or model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    # Model and additional fields that we want to pass to serializer
    class Meta:
        model = get_user_model()
        # Fields that will be enabled for serializer
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
    
    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)