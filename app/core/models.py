"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# AbstractBaseUser:Contains functionality for authentication system
# PermissionError:Contains funcationality for permission feature


class UserManager(BaseUserManager):
    """Manager for Users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionError):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # Determine if user can login as Django Admin
    is_staff = models.BooleanField(default=True)
    # Assign UserManager to custom User Class
    objects = UserManager()
    # The field that will be used for authentication.
    # Replaces default user model authentication field to email
    USERNAME_FIELD = 'email'
