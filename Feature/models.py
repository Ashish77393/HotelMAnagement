from django.db import models
class Featuresdata(models.Model):
    image=models.ImageField()
    header=models.CharField(max_length=50)
    des=models.CharField(max_length=200)

# Create your models here.
