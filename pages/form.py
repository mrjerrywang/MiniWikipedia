from django import forms
from .models import *

class createPlayerForm(forms.ModelForm):

    class Meta: #assciate this form with player model  
        model = Player
        fields = ['gameTag', 'name', 'teamName', ]

class updatePlayerForm(forms.ModelForm):

    class Meta:
        model = Player #assciate this form with player model
        fields = ['gameTag', 'name', 'teamName', ]

class createMatchForm(forms.ModelForm):

    class Meta: #assciate this form with Game model  
        model = Game
        fields = ['gameId', 'team1', 'team2', 'times']

class updateMatchForm(forms.ModelForm):

    class Meta:
        model = Game #assciate this form with Game model
        fields = ['gameId', 'team1', 'team2', 'times']
    
class createTeamForm(forms.ModelForm):

    class Meta: #assciate this form with Team model  
        model = Team
        fields = ['name', 'region', 'teamIcon', 'member1', 'member2', 'member3', 'member4', 'member5',]

class updateTeamForm(forms.ModelForm):

    class Meta:
        model = Team #assciate this form with Team model
        fields = ['name', 'region', 'teamIcon', 'member1', 'member2', 'member3', 'member4', 'member5',]
