from django.db import models

# Create your models here.
class modelname(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Email = models.EmailField()
