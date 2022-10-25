from email.policy import default
from django.urls import reverse
from django.db import models

# Provides choices 
RESULTS = (
    ('W', 'Win'),
    ('L', 'Loss'),
)
POSITIONS = (
    ('QB', 'Quarterback'),
    ('RB', 'Running Back'),
    ('WR', 'Wide Receiver'),
    ('TE', 'Tight End'),
    ('K', 'Kicker'),
    ('DEF', 'Defense'),
)

class Player(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(
        max_length=3,
        choices=POSITIONS,
        default=[0][0],
        )
    nfl_team = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('players_detail', kwargs={'pk': self.id})

# Team model
class Team(models.Model):
    # Name and league are character fields
    name = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    players = models.ManyToManyField(Player)
    
    # Says its name
    def __str__(self):
        return self.name

    # Redirects to detail page upon creation of team
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'team_id': self.id})

# Record model
class Record(models.Model):
    # Week is an integer field and result is a char field that utilizes a dropdown menu
    week = models.IntegerField()
    result = models.CharField(
        max_length=1,
        choices=RESULTS,
        default=RESULTS[0][0],
        )
    # Links the foreign key (team primary key)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    # Makes it say its name
    def __str__(self):
        return f"{self.get_result_display()} on Week {self.week}"

    # Changes the default sort
    class Meta:
        ordering = ['week']