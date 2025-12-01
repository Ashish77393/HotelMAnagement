from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from HotelList.models import HotelList, BookHotel
from Carasoul.models import Carasoul
from contact.models import contact
from Studentsign.models import Studentsign


def home(request):
    # Redirect already-logged users to dashboard
    if request.session.get("user_id") and request.method != "POST":
        return redirect("/Dashboard")

    if request.method == "POST":
        email = (request.POST.get("email") or "").strip()
        password = request.POST.get("password") or ""

        if not email or not password:
            return render(request, "home.html", {"error": "Email and password are required!"})

        user = Studentsign.objects.filter(email=email, password=password).first()
        if user:
            # Save login in session
            request.session["user_id"] = user.id
            request.session["user_name"] = user.name
            messages.success(request, f"Welcome back, {user.name}!")
            return redirect("/Dashboard")

        return render(request, "home.html", {"error": "Invalid email or password"})

    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        name = request.POST.get("name") or ""
        email = (request.POST.get("email") or "").strip()
        password = request.POST.get("password") or ""
        contact_val = request.POST.get("tel") or ""

        if not name or not email or not password:
            messages.error(request, "Please provide name, email and password to sign up.")
            return render(request, "SignUpPage.html")

        # Prevent duplicate signups with same email
        if Studentsign.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, "SignUpPage.html")

        s = Studentsign(name=name, email=email, password=password, contact=contact_val)
        s.save()

        # Auto-login after signup
        request.session["user_id"] = s.id
        request.session["user_name"] = s.name
        messages.success(request, "Signup successful — you are now logged in.")
        return redirect("/Dashboard")

    return render(request, "SignUpPage.html")


def Dashboard(request):
    hotel = HotelList.objects.all()
    carasoul = Carasoul.objects.all()

    total_hotels = hotel.count()
    total_bookings = BookHotel.objects.count()
    avg_rating = 0
    if total_hotels:
        avg_rating = int(sum(h.rating for h in hotel) / total_hotels)

    return render(request, "Dashboard.html", {
        "hotel": hotel,
        "carasoul": carasoul,
        "total_hotels": total_hotels,
        "total_bookings": total_bookings,
        "avg_rating": avg_rating,
    })


def BookNow(request):
    if request.method == "POST":
        checkin = request.POST.get("checkin")
        checkout = request.POST.get("checkout")
        numberofpeople = request.POST.get("numberofpeople")

        b = BookHotel()
        b.CheakinDate = checkin
        b.CheakoutDate = checkout
        b.guest = numberofpeople
        b.save()
        messages.success(request, "Booking request received.")

    return render(request, "Book.html", {})


def Payment(request):
    return render(request, "Payment.html", {})


def logout_view(request):
    request.session.flush()
    messages.info(request, "You have been logged out.")
    return redirect("/")



