"""
Test for admin
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminTest(TestCase):
    """Test for Django admin"""

    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="testpass123",
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="testpass123",
            name="Test user",
        )

    def test_admin_list(self):
        ulr = reverse("admin:core_user_changelist")
        res = self.client.get(ulr)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
