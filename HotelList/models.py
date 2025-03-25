from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class HotelList(models.Model):
    image=models.ImageField()
    header=models.CharField(max_length=100)
    price=models.IntegerField()
    rating=models.IntegerField()
    facility=models.CharField(max_length=200)
    des=models.TextField(max_length=500)
class BookHotel(models.Model):
    CheakinDate=models.DateField()
    CheakoutDate=models.DateField()
    guest=models.CharField(max_length=1)