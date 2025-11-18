from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def about_us(request):
    return render(request, "aboutus/about.html")