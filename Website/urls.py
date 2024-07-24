"""
URL configuration for stu_mng_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("land-inventory",views.land_inventory,name="land_inventory"),
    path("applicant",views.applicant,name='applicant'),
    path("app_payment", views.app_payment, name="app_payment"),
    path("app_profile", views.app_profile, name="app_profile"),
    path("app_status", views.app_status, name="app_status"),

    path("contact_us",views.contact_us,name="contact_us"),
    path("drone",views.drone,name='drone'),
    path("implementing_home", views.implementing_home, name="implementing_home"),
    path("nodal", views.nodal, name="nodal")
    
]
