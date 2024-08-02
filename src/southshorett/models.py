from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Season(models.Model):
    name = models.CharField(max_length=64)
    start = models.DateField()
    end = models.DateField()


class Match(models.Model):
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="wins")
    loser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="losses")
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    when = models.DateTimeField()


class Rating(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    elo = models.IntegerField()
