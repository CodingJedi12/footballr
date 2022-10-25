from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import RecordForm

from .models import Player, Record, Team

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
    # Creates a win and loss variable to be used
    wins = 0
    losses = 0
    # Assings the team variable to a specific id in the Team model object that is passed as an argument
    team = Team.objects.get(id=team_id)
    # Attaches a variable to the record model and its objects
    records = Record.objects.all()
    # Allows for us to use the form in our detail template
    record_form = RecordForm()
    # Get players that are not on team
    players_not_on_team = Player.objects.exclude(id__in = team.players.all().values_list('id'))

    # Goes through the records for the team and tallies wins and losses
    for record in records:
        if record.team_id == team.id:
            if record.result == "W":
                wins += 1
            if record.result == "L":
                losses += 1
        
    # Renders the request, the detail template and passes the team variable through
    return render(request, 'teams/detail.html', {
        'team': team,
        'wins': wins,
        'losses': losses,
        'record_form': record_form,
        'players': players_not_on_team,
        })

def add_game(request, team_id):
    # Sets form equal to the post request of a completed game form
    form = RecordForm(request.POST)
    # If the form is valid, we save it, set the id equal to the orignating id and then save it
    if form.is_valid():
        new_game = form.save(commit=False)
        new_game.team_id = team_id
        new_game.save()
    return redirect('detail', team_id=team_id)

# Creates a new team using the Team model and reroutes upon success
class TeamCreate(CreateView):
    model = Team
    fields = '__all__'
    success_url = '/myteams/'

# Updates an existing team
class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'

# Deletes an existing team and reroutes upon success
class TeamDelete(DeleteView):
    model = Team
    success_url = '/myteams/'

# Allows the player to be linked to the team
def assoc_player(request, team_id, player_id):
    Team.objects.get(id=team_id).players.add(player_id)
    return redirect('detail', team_id=team_id)

# Links model with index template
class PlayerList(ListView):
    model = Player
    template_name = 'players/index.html'

# Links model with detail template
class PlayerDetail(DetailView):
    model = Player
    template_name = 'players/detail.html'