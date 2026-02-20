from django.shortcuts import render,redirect
from .models import UserData


# Create your views here.

def index(request) :
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        age = request.POST.get("age")
        city = request.POST.get("city")
        message = request.POST.get("message")
        
        UserData.objects.create(
            fullname=fullname,
            email=email,
            username = username,
            password = password,
            phone = phone,
            age = age,
            city = city,
            message = message
        )
        return redirect("index")
    
    return render(request,"universityapps/university.html")