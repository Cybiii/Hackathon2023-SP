from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Website/home.html')

def one(request):
    return render(request, 'Website/one.html')

def two(request):
    return render(request, 'Website/two.html')

