"""
Tests for the Django admin modifications.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    # A special method to run before every single test. Naming is important
    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        # Force authentication with user created
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_list(self):
        """Test that users are listed on page."""
        # URL to be pulled from Django Admin for User list
        # Check Django documentation Reversing admin URLs
        url = reverse('admin:core_user_changelist')
        # Simulates HTTP GET request
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test that users can be editted on page"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        # Check page loads successfully
        self.assertEqual(res.status_code, 200)
