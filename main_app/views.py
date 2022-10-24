from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Team

# Create your views here.
# Renders the home page by connecting to the home.html template
def home(request):
    return render(request, 'home.html')

# Renders the about page by connecting to the about.html template
def about(request):
    return render(request, 'about.html')

# Renders the my teams page by connecting to the template
def teams_index(request):
    # Assigns a variable to the entire Team model object
    teams = Team.objects.all()
    # Renders the type of request, routes to the teams template, and passes the variable we made into the template to be used
    return render(request, 'teams/index.html', {'teams': teams})

# Renders the team detail (show) page by connecting to the template
def teams_detail(request, team_id):
    # Assings the team variable to a specific id in the Team model object that is passed as an argument
    team = Team.objects.get(id=team_id)

    # Renders the request, the detail template and passes the team variable through
    return render(request, 'teams/detail.html', {'team': team})

class TeamCreate(CreateView):
    model = Team
    fields = '__all__'
    success_url = '/myteams/'

class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'

class TeamDelete(DeleteView):
    model = Team
    success_url = '/myteams/'