from django.db import models
class about(models.Model):
    header1=models.CharField(max_length=50)
    header1_des=models.CharField(max_length=300)
    header2=models.CharField(max_length=50)
    header2_des=models.CharField(max_length=300)
    header3=models.CharField(max_length=50)
    header3_des1=models.CharField(max_length=100)
    header3_des2=models.CharField(max_length=100)
    header3_des3=models.CharField(max_length=100)
    header3_des4=models.CharField(max_length=100)
    header4=models.CharField(max_length=40)
    header4_des=models.CharField(max_length=300)
    header5=models.CharField(max_length=40)
    header5_des=models.CharField(max_length=500)
# Create your models here.
