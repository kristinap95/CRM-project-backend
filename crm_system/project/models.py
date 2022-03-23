from django.db import models
from user.models import Account
from datetime import date

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    CHOICES_STATUS = (
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed')
    )
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default='New')
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
