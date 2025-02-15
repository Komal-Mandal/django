from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home1(requests):
    return HttpResponse("home page1")