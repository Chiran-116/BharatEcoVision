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
    path("applicant",views.applicant,name='applicant')
    # path("all_stu", views.all_stu, name="all_stu"),
    # path("add_stu", views.add_stu, name="add_stu"),
    # path("rm_stu", views.rm_stu, name="rm_stu"),
    # path('rm_stu/<str:USN>/', views.rm_stu, name='rm_stu_detail'),
    # path("filter_stu", views.filter_stu, name="filter_stu"),
    # path('take_attendance', views.take_attendance, name='take_attendance'),
    # path('view_attendance', views.view_attendance, name='view_attendance'),
    # path('course_attendance', views.course_attendance, name='course_attendance'),
    # path('course_attendance/<int:Course_id>/<str:date>/', views.course_attendance, name='course_attendance_report'),
    # path('course_attendance_shortage',views.course_attendance_shortage,name = "course_attendance_shortage")
]
