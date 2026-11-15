from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class PlayerCharacter(models.Model):
    class CharacterClass(models.TextChoices):
        ARTIFICER = 'ARTIFICER', 'Artificer'
        BARBARIAN = 'BARBARIAN', 'Barbarian'
        BARD = 'BARD', 'Bard'
        CLERIC = 'CLERIC', 'Cleric'
        DRUID = 'DRUID', 'Druid'
        FIGHTER = 'FIGHTER', 'Fighter'
        MONK = 'MONK', 'Monk'
        PALADIN = 'PALADIN', 'Paladin'
        RANGER = 'RANGER', 'Ranger'
        ROGUE = 'ROGUE', 'Rogue'
        SORCERER = 'SORCERER', 'Sorcerer'
        WARLOCK = 'WARLOCK', 'Warlock'
        WIZARD = 'WIZARD', 'Wizard'

    name = models.CharField(max_length=200)
    character_class = models.CharField(
        max_length=30,
        choices=CharacterClass.choices,
        default=CharacterClass.ARTIFICER,
    ) # TODO: enable multiclassing
    level = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(20)])
    notes = models.TextField(blank=True)
    player_name = models.CharField(max_length=200)
