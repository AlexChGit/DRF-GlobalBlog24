from django.db import models
import jwt
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class UserManager(BaseUserManager):
    """ UserManager for custom User. """

    def create_user(self, email, password=None):
        """ Creates a User with email and password. """
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """ Creates a Superuser. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ A class to represent a user. """
    username = models.CharField(db_index=True, max_length=120, blank=True)
    lastname = models.CharField(db_index=True, max_length=120, blank=True)
    phone_number = PhoneNumberField(db_index=True, blank=True)
    email = models.EmailField(db_index=True, unique=True, blank=True)
    about = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        """ String representation of the model. """
        return self.email

    def get_full_name(self):
        full_name = '%s %s' % (self.username, self.lastname)
        return full_name.strip()

    def get_short_name(self):
        return self.username





