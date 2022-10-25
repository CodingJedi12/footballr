from email.policy import default
from django.urls import reverse
from django.db import models

# Provides choices 
RESULTS = (
    ('W', 'Win'),
    ('L', 'Loss'),
)

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'team_id': self.id})

class Record(models.Model):
    week = models.IntegerField()
    result = models.CharField(
        max_length=1,
        choices=RESULTS,
        default=RESULTS[0][0],
        )
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    # Makes it say its name
    def __str__(self):
        return f"{self.get_result_display()} on Week {self.week}"

    # Changes the default sort
    class Meta:
        ordering = ['week']