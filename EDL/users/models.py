from django.db import models

class Human(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=256)
 #Create your models here.
