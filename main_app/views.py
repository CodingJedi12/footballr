from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Team

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def my_teams(request):
    teams = Team.objects.all()
    return render(request, 'teams/index.html', {'teams': teams})