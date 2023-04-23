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
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # Function name is important. Django CLI will use method with this name
    def create_superuser(self, email, password):
        """Create and return the super-user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # Determine if user can login as Django Admin
    is_staff = models.BooleanField(default=False)
    # Assign UserManager to custom User Class
    objects = UserManager()
    # The field that will be used for authentication.
    # Replaces default user model authentication field to email
    USERNAME_FIELD = 'email'
