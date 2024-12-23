from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=10, choice=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.username
    

class Product(models):
    name = models.CharField(max_length=50)
    price = models.FloatField