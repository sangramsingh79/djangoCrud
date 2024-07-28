from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=2)
    Email = models.EmailField()
    Password = models.CharField(max_length=30)
    