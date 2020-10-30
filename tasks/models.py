from django.db import models

# Create your models here.
class Task(models.Model):
    task_name=models.CharField(max_length=200)
    task_start=models.CharField(max_length=200)
    task_end=models.CharField(max_length=200)
    status=models.CharField(max_length=200)