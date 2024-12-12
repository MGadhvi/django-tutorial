from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world, You're at the polls index")

def welcome(request):
    return HttpResponse("This is another request")
