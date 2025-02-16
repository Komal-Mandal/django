from django.shortcuts import render
from . import views

def learn_django(req):
    return render(req,"app4/django.html")
