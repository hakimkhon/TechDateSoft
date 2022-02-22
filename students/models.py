from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Student(models.Model):
    ism = models.CharField(max_length=15)
    famila = models.CharField(max_length=15)
    yosh = models.IntegerField(default=0)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ism)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
            return str(self.user)
    