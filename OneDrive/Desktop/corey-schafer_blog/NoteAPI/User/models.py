from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='User-Name',
        error_messages={'unique': "A user with that username already exists."},
    )

    def __str__(self):
        return f'{self.username} is a user'