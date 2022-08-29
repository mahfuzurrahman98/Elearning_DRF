from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    institute = models.CharField(max_length=150)
    department = models.CharField(max_length=50)
