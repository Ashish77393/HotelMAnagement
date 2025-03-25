from django.db import models

class Studentsign(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    contact=models.CharField(max_length=10)
def __str__(self):
    return self.name
