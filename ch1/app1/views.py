from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myfunction(request):
    return HttpResponse("hello world")


def home(request):
    return HttpResponse("home page")
