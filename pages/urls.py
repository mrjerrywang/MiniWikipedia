from django.urls import path
from .views import * #HomePageView,AboutPageView,TeamPageView,SingleTeamView,MatchPageView,PlayerPageView,SinglePlayerView,MatchPageView,SingleMatchView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('teams', TeamPageView.as_view(), name='teams'),    #show all teams
    path('team/<int:pk>', SingleTeamView.as_view(), name='team'),   #show single team
    path('team/<int:pk>/update', updateTeamView.as_view(), name='updateTeam'),
    path('team/<int:pk>/delete', deleteTeamView.as_view(), name='deleteTeam'),
    path('players', PlayerPageView.as_view(), name='players'),
    path('player/<int:pk>', SinglePlayerView.as_view(), name='player'),
    path('player/<int:pk>/update', updatePlayerView.as_view(), name='updatePlayer'),
    path('player/<int:pk>/delete', deletePlayerView.as_view(), name='deletePlayer'),
    path('matches', MatchPageView.as_view(), name='matches'),
    path('match/<int:pk>', SingleMatchView.as_view(), name='match'),
    path('match/<int:pk>/update', updateMatchView.as_view(), name='updateMatch'),
    path('match/<int:pk>/delete', deleteMatchView.as_view(), name='deleteMatch'),
    path('createPlayer', createPlayerView.as_view(), name='createPlayer'),
    path('createMatch', createMatchView.as_view(), name='createMatch'),
    path(' ', createTeamView.as_view(), name='createTeam'),
]