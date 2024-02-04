from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=20)
    cls=models.CharField
    marks=models.IntegerField
    Totalmarks=models.IntegerField
    
    