from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from accounts import views
urlpatterns = [
# Used for making the function call to views.py in apps- > calc
    path('register',views.register,name = 'register'),
    path('login',views.login,name = "login"),
    path('logout',views.logout,name = "logout")
]
