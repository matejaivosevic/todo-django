from django.db import models
from django.core import serializers

class Item(models.Model):
    def __str__(self):
            return self.title

    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400)
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
    completed = models.BooleanField(default=False)

class User(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
