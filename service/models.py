from django.db import models
class service(models.Model):
 image=models.ImageField()
 header=models.CharField(max_length=200)
 des=models.CharField(max_length=400)
# Create your models here.
