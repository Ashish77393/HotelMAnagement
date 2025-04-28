from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.TextField(max_length=1000)
def __str__(self):
    return self.name
class contactPersonalDetails(models.Model):
    header=models.CharField(max_length=100)
    mess=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
