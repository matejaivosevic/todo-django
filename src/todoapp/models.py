from django.db import models
from django.core import serializers
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

class User(AbstractBaseUser):
    email = models.CharField(max_length=200, null=False, unique=True)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Item(models.Model):
    def __str__(self):
            return self.title

    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400)
    completed = models.BooleanField(default=False),
    PRIORITY = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY,
        default='Low',
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
