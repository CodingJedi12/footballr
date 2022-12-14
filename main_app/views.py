from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
@login_required
def teams_index(request):
    # Assigns a variable to the entire Team model object
    teams = Team.objects.filter(user=request.user)
    # Renders the type of request, routes to the teams template, and passes the variable we made into the template to be used
    return render(request, 'teams/index.html', {'teams': teams})

# Renders the team detail (show) page by connecting to the template
@login_required
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

@login_required
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
class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = ('name', 'league')
    success_url = '/myteams/'

    # If Valid Team form is received on submission
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        # Let the CreateView behave normally
        return super().form_valid(form)

# Updates an existing team
class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = '__all__'

# Deletes an existing team and reroutes upon success
class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = '/myteams/'

# Allows the player to be linked to the team
@login_required
def assoc_player(request, team_id, player_id):
    Team.objects.get(id=team_id).players.add(player_id)
    return redirect('detail', team_id=team_id)

# Links model to create template
class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ('name', 'position', 'nfl_team')

# Links model to update template
class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ('name', 'position', 'nfl_team')

# Links model to delete template
class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players'

# Links model with index template
class PlayerList(LoginRequiredMixin, ListView):
    model = Player
    template_name = 'players/index.html'

# Links model with detail template
class PlayerDetail(LoginRequiredMixin, DetailView):
    model = Player
    template_name = 'players/detail.html'

# Signup view
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how we create a 'user' form object that allows us to use data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
