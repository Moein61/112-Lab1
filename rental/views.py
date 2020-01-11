from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def test (requst):
    return HttpResponse("this is a test page!")

def developer(request):
    return HttpResponse("<h1>Moein Ghomeshian</h1>")