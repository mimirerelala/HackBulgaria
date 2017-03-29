from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)