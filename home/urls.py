from . import views

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('home',views.home,name='index')
]