from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('myteams/', views.teams_index, name='index'),
    path('myteams/<int:team_id>/', views.teams_detail, name='detail'),
    path('myteams/create/', views.TeamCreate.as_view(), name='teams_create'),
    path('myteams/<int:pk>/update/', views.TeamUpdate.as_view(), name='teams_update'),
    path('myteams/<int:pk>/update/', views.TeamDelete.as_view(), name='teams_delete'),
]