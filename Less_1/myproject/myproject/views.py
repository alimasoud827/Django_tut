# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("<h1>Hello, world!</h1>") 
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("My about Page")
    return render(request, 'about.html')