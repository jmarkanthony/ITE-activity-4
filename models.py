from django.db import models
from django.forms import CharField

# Create your models here.
class users(models.Model):
     username = models.CharField(max_length=255)
     password = models.CharField(max_length=255)
     confirmpassword = models.CharField(max_length=255)
     
     def __str__(self):
        return self.username



class Student(models.Model):
    sid = models.CharField(max_length=4)
    sname = models.CharField(max_length=255)
    scontact = models.CharField(max_length=15)

    def __str__(self):
        return self.sname
        
