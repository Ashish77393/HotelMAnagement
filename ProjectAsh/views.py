from django.shortcuts import render
from django.shortcuts import redirect
from HotelList.models import HotelList,BookHotel
from Carasoul.models import Carasoul
from contact.models import contact

from django.http import HttpResponse
from Studentsign.models import Studentsign
def home(request):
     if request.method == "POST":
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = Studentsign.objects.filter(password=password, email=email).first()
        print(user)
        if not email or not password:
            return render(request, "home.html", {"error": "Email and password are required!"})

        user = Studentsign.objects.filter(email=email, password=password).first()
        if user:
            return  redirect("/Dashboard") # Change "dashboard" to 
        else:
            # return HttpResponse("<h1>User DOes not exits</h1>")
            return render(request, "home.html", {"error": "Invalid name or email"})
     return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        contact = request.POST.get("tel")
        s=Studentsign()
        s.name=name
        s.email=email
        s.password=password
        s.contact=contact
        s.save()
        return redirect("/")
    return render(request, "SignUpPage.html")

        # e=Student()
        # e.name=student_name
        # e.email=student_email
        # e.password=student_password
        # e.contact=student_contact
        # e.save()
          
def Dashboard(request):
    hotel=HotelList.objects.all()
    carasoul=Carasoul.objects.all()
    return render(request,"Dashboard.html",{"hotel":hotel,"carasoul":carasoul})
def BookNow(request):
    if request.method=="POST":
     checkin=request.POST.get('checkin')
     checkout=request.POST.get('checkout')
     numberofpeople=request.POST.get('numberofpeople')
     print(checkin)
     b=BookHotel()
     b.CheakinDate=checkin
     b.CheakoutDate=checkout
     b.guest=numberofpeople  
     b.save() 
    return render(request,"Book.html",{})
def Payment(request):
    return render(request,'Payment.html',{})



