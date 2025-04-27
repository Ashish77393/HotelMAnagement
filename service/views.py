from django.shortcuts import render
from .models import service
def Services(request):
    servi=service.objects.all()
    return render(request,'Services.html',{"service":servi})
# Create your views here.
