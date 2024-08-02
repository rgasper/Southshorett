from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class MyBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Player(MyBaseModel):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Season(MyBaseModel):
    name = models.CharField(max_length=64)
    start = models.DateField()
    end = models.DateField()
    players = models.ManyToManyField(Player, through="Rating")

    def __str__(self):
        return self.name

    @classmethod
    def get_current(cls) -> "Season":
        return cls.objects.get(start__lte=datetime.now(), end__gt=datetime.now())


class Match(MyBaseModel):
    class Meta:
        verbose_name_plural = "matches"

    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="wins")
    loser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="losses")
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="matches")
    when = models.DateTimeField()

    def __str__(self):
        return f"{self.winner.name} vs {self.loser.name} on {self.when.strftime('%m/%d/%Y')}"


class Rating(MyBaseModel):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="ratings")
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="ratings")
    elo = models.IntegerField()

    def __str__(self):
        return f"{self.player.name}'s Rating"
