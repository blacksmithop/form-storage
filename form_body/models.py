from operator import mod
from pyexpat import model
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    email = models.EmailField()
    # document = models.ImageField()
    avatar = models.FileField()
