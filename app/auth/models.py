# app/auth/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Nome relacionado único para evitar conflitos
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Nome relacionado único para evitar conflitos
        blank=True,
        help_text='Specific permissions for this user.'
    )
