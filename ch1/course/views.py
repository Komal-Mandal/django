from django.shortcuts import render
from django.http import HttpResponse

def course(request):
    return HttpResponse("hello")


