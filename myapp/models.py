from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(User,max_length=100)
    password = models.CharField(max_length=100)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)