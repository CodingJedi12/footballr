from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('myteams/', views.teams_index, name='index'),
    path('myteams/<int:team_id>/', views.teams_detail, name='detail'),
    path('myteams/create/', views.TeamCreate.as_view(), name='teams_create'),
    path('myteams/<int:pk>/update/', views.TeamUpdate.as_view(), name='teams_update'),
    path('myteams/<int:pk>/delete/', views.TeamDelete.as_view(), name='teams_delete'),
    path('myteams/<int:team_id>/add_game/', views.add_game, name='add_game'),
    path('myteams/<int:team_id>assoc_player/<int:player_id>/', views.assoc_player, name='assoc_player'),
    path('players/', views.PlayerList.as_view(), name='players_index'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='players_detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete')
]

