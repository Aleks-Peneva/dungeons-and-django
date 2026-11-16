from django.core.validators import MinValueValidator
from django.db import models
from character.models import PlayerCharacter
from django.urls import reverse


class Quest(models.Model):
    class QuestStatus(models.TextChoices):
        UNDISCOVERED = 'UNDISCOVERED', 'Undiscovered'
        DISCOVERED = 'DISCOVERED', 'Discovered'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        FAILED = 'FAILED', 'Failed'

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    involved_characters = models.ManyToManyField(
        PlayerCharacter,
        blank=True,
        related_name='quest'
    )
    awarding_XP = models.IntegerField(
        default=1000,
        validators=[MinValueValidator(1000)])
    status = models.CharField(
        max_length=20,
        choices=QuestStatus.choices,
        default=QuestStatus.UNDISCOVERED,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_status_display()}] {self.title}"

    def get_absolute_url(self):
        return reverse('quest:detail', kwargs={'pk': self.pk})

    def party_size(self):
        return self.involved_characters.count()
