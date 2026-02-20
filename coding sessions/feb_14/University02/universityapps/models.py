from django.db import models

# Create your models here.


class UserData(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    age = models.IntegerField()
    city = models.CharField( max_length=100)
    message = models.CharField( max_length=500)
    
    def __str__(self):
        return f"{self.fullname} -- {self.username}"
    