from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

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

    class CharacterRace(models.TextChoices):
        HUMAN = 'HUMAN', 'Human'
        DWARF = 'DWARF', 'Dwarf'
        ELF = 'ELF', 'Elf'
        HALFLING = 'HALFLING', 'Halfling'
        DRAGONBORN = 'DRAGONBORN', 'Dragonborn'
        GNOME = 'GNOME', 'Gnome'
        HALF_ELF = 'HALF_ELF', 'Half-Elf'
        HALF_ORC = 'HALF_ORC', 'Half-Orc'
        ORC = 'ORC', 'Orc'
        TIEFLING = 'TIEFLING', 'Tiefling'

    name = models.CharField(max_length=200, unique=True)
    character_class = models.CharField(
        max_length=30,
        choices=CharacterClass.choices,
        default=CharacterClass.ARTIFICER,
    ) # TODO: enable multiclassing and homebrew
    character_race = models.CharField(
        max_length=30,
        choices=CharacterRace.choices,
        default=CharacterRace.HUMAN,
    ) # TODO: enable homebrew
    # TODO: add background with 5e choices
    level = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1, message="Character level cannot drop below level 1."),
            MaxValueValidator(20, message="Maximum level reached."),
        ]
    )
    notes = models.TextField(blank=True)
    player_name = models.CharField(max_length=200)
    alive = models.BooleanField(default=True)

    class Meta:
        ordering = ['-level', 'name']

    def __str__(self):
        return f"{self.player_name} (Level {self.level} {self.character_class})"


class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    character = models.ForeignKey(
        PlayerCharacter,
        on_delete=models.CASCADE,
        related_name='inventory',
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1, message="Item quantity must be at least 1.")
        ],
    )
    requires_attunement = models.BooleanField(default=False)
    is_attuned = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.quantity} {self.name}(s))"