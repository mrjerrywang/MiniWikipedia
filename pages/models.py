from django.db import models
from django.urls import reverse #get url from pattern name

# Create your models here.
class Player(models.Model):
    gameTag = models.TextField(blank=False)
    name = models.TextField(blank=True)
    teamName = models.TextField(blank=True)
    picture = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse("player", kwargs={"pk": self.pk})

    def __str__(self):
        return 'Ingame ID: %s \n Name: %s\nTeam: %s' %(self.gameTag, self.name, self.teamName)

class Team(models.Model):
    name = models.TextField(blank=True)
    region = models.TextField(blank=True)
    teamIcon = models.URLField(blank=True)
    
    member1 = models.ForeignKey('Player', related_name='player1', blank=True, on_delete=models.CASCADE)
    member2 = models.ForeignKey('Player', related_name='player2', blank=True, on_delete=models.CASCADE)
    member3 = models.ForeignKey('Player', related_name='player3', blank=True, on_delete=models.CASCADE)
    member4 = models.ForeignKey('Player', related_name='player4', blank=True, on_delete=models.CASCADE)
    member5 = models.ForeignKey('Player', related_name='player5', blank=True, on_delete=models.CASCADE) # on_delete=models.SET_NULL, null = True) can be deleted
    
    def getMatches(self):
        matches = Team.objects.filter(team = self.pk)
        return matches

    def get_absolute_url(self):
        return reverse("team", kwargs={"pk": self.pk})

    def __str__(self):
        return 'Team %s (%s)' % (self.name, self.region)


class Game(models.Model):
    gameId = models.AutoField(primary_key=True)
    team1 = models.ForeignKey('Team', related_name='blueTeam', blank=True, on_delete=models.CASCADE)
    team2 = models.ForeignKey('Team', related_name='redTeam', blank=True, on_delete=models.CASCADE)
    times = models.DateField()

    def get_absolute_url(self):
        return reverse("match", kwargs={"pk": self.pk})

    def __str__(self):
        return 'Game ID %d: %s vs %s (%s)' % (self.gameId, self.team1, self.team2, self.times)

        