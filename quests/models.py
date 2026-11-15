from django.core.validators import MinValueValidator
from django.db import models
from playerCharacters.models import PlayerCharacter


class Quest(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    involved_characters = models.ManyToManyField(
        PlayerCharacter,
        blank=True,
        related_name='quests'
    )
    awarding_XP = models.IntegerField(
        default=1000,
        validators=[MinValueValidator(1000)])
    status = models.CharField(max_length=200)