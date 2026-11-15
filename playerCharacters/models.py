from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=200)
    character_class = models.CharField(max_length=200)
    level = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(20)])
    notes = models.TextField(blank=True)
    player_name = models.CharField(max_length=200)
