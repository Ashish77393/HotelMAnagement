from django.shortcuts import render
from .models import about
def About(request):
    data=about.objects.all()
    return render(request,'About.html',{"about":data})
# Create your views here.
