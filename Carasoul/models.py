from django.db import models

# Create your models here.
class Carasoul(models.Model):
  image=models.ImageField()
  heading=models.CharField(max_length=300)
  description=models.TextField(max_length=1000)
def __str__(self):
    return self.heading
