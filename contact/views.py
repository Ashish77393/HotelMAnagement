from django.shortcuts import render
from .models import contact,contactPersonalDetails
from django.contrib import messages

def Contact(request):
    personaldata = contactPersonalDetails.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get('message')

        c = contact()
        c.name = name
        c.email = email
        c.message = message
        c.save()

        messages.success(request, "Your message has been sent successfully!")

    return render(request, 'Contact-Us.html', {"personal": personaldata})
