from django.db import models

class Question(models.Model):
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
