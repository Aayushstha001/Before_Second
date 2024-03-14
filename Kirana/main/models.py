from django.db import models

# Create your models here.


class form(models.Model):

    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length= 30)
    repassword = models.CharField(max_length= 30)