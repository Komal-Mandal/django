from django.shortcuts import render

# Create your views here.

def learn_django(req):
    return render(req,"app6/django.html")
