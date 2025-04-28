from django.shortcuts import render
from .models import Featuresdata
def Features(request):
    data=Featuresdata.objects.all()
    return render(request,'Features.html',{"feature":data})
# Create your views here.
