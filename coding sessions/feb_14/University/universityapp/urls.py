from django.urls import path

from . import views


urlpatterns = [
        path("",views.index,name = "index"),
        path("library/",views.library,name = "library"),
        path("students/",views.students,name = "students"),
        path("teachers/",views.teachers,name = "teachers"),
        path("admissions/",views.teachers,name = "admissions"),
        path("aboutus/",views.teachers,name = "aboutus"),
]