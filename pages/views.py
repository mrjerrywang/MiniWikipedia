from django.shortcuts import render
from django.views.generic import * #TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import * #Team,Game,Player
from .form import * #createPlayerForm, updatePlayerForm, createMatchForm, updateMatchForm, createTeamForm, updateTeamForm

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class TeamPageView(ListView):
    model = Team
    template_name = 'pages/teams.html'
    context_object_name = 'all_teams_list'

class SingleTeamView(DetailView):
    model = Team
    template_name = 'pages/team.html'
    context_object_name = 'team'

class PlayerPageView(ListView):
    model = Player
    template_name = 'pages/players.html'
    context_object_name = 'all_players_list'

class SinglePlayerView(DetailView):
    model = Player
    template_name = 'pages/player.html'
    context_object_name = 'player'

class MatchPageView(ListView):
    model = Game
    template_name = 'pages/matches.html'
    context_object_name = 'all_matches_list'

class SingleMatchView(DetailView):
    model = Game
    template_name = 'pages/match.html'
    context_object_name = 'game'

class createPlayerView(CreateView):
    form_class = createPlayerForm
    template_name = 'pages/createPlayer.html'

class updatePlayerView(UpdateView):
    form_class = updatePlayerForm
    template_name = 'pages/updatePlayer.html'
    queryset = Player.objects.all()

class deletePlayerView(DeleteView):
    template_name = 'pages/deletePlayer.html'
    queryset = Player.objects.all()
    success_url = "../../players"

class createMatchView(CreateView):
    form_class = createMatchForm
    template_name = 'pages/createMatch.html'

class updateMatchView(UpdateView):
    form_class = updateMatchForm
    template_name = 'pages/updateMatch.html'
    queryset = Game.objects.all()

class deleteMatchView(DeleteView):
    template_name = 'pages/deleteMatch.html'
    queryset = Game.objects.all()
    success_url = "../../matches"

class createTeamView(CreateView):
    form_class = createTeamForm
    template_name = 'pages/createTeam.html'

class updateTeamView(UpdateView):
    form_class = updateTeamForm
    template_name = 'pages/updateTeam.html'
    queryset = Team.objects.all()

class deleteTeamView(DeleteView):
    template_name = 'pages/deleteTeam.html'
    queryset = Team.objects.all()
    success_url = "../../teams"

