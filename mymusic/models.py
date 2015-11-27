from django.db import models

# Create your models here.

class Userdetails(models.Model):
	firstname = models.CharField(max_length=140)
	lastname = models.CharField(max_length=140)
	email = models.EmailField(unique = True)
	password = models.CharField(max_length=20)
	mobilenumber = models.CharField(max_length=15, unique=True)