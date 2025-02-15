from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def hello(requests):
    return HttpResponse("hello world")

def home(requests):
    return HttpResponse("home page")