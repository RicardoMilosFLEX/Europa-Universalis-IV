from django.db import models
from django.contrib.auth.models import AbstractUser


class NewUser(AbstractUser):
    login = models.CharField('login', max_length=255, default='')
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)