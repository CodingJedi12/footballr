from django.urls import reverse
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'team_id': self.id})