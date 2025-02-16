from django.shortcuts import render
from . import views

# variable example 1
"""def  learn_django(req):
    return render(req,"app5/django.html",context={"name":"django"} )"""

# variable example 2
'''def  learn_django(req):

    name = "django"
    duration = "4 months"
    seats = 10
    detail = {"nm":name, "du":duration,"st":seats}

    return render(req,"app5/django.html",detail )'''

# example 2 - Filters

def  learn_django(req):
    return render(req,"app5/django.html",context={"name":"django", "desc":"django is the awesome web programming"} )

