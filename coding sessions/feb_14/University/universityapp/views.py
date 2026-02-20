from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"universityapp/index.html")


def library(request):
    return render(request,"universityapp/library.html")


def students(request):
    return render(request,"universityapp/students.html")


def teachers(request):
    return render(request,"universityapp/teachers.html")


def admissions(request):
    return render(request,"universityapp/admissions.html")


def aboutus(request):
    return render(request,"universityapp/aboutus.html")

