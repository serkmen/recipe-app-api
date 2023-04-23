"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models."""
    email = 'test@example.com'
    password = 'testpass123'
    user = get_user_model().objects.create_user(
        email=email,
        password=password,
    )
    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))
