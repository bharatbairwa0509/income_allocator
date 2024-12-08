from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dic(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    income = models.IntegerField(default=0)
    rent = models.IntegerField(default=0)
    transport = models.IntegerField(default=0)
    other = models.IntegerField(default=0)
    entertainment = models.IntegerField(default=0)
    date = models.DateField()
    


    def __str__(self):
        return "user is"
