"""
Views for the user API.
"""
from rest_framework import generics
from user.serializers import UserSerializer


# Handles POST requests to create user
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
