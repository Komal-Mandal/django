from django.shortcuts import render  # Correct import

def home(request):
    return render(request, 'index.html')  # Correct usage


# Create your views here.
