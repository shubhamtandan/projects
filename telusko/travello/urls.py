from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from travello import views
urlpatterns = [
# Used for making the function call to views.py in apps- > calc
    path('',views.index,name = 'index')
]
