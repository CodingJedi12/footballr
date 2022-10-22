from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home page")

def about(request):
    return HttpResponse("About page")

def my_teams(request):
    return HttpResponse("My Teams Page")