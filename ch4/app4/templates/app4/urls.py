from django.contrib import admin
from django.urls import path
from app4.views import learn_django

urlpatterns = [
    path("dj/","learn_django")
]
