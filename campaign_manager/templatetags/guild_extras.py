from django import template
from character.models import PlayerCharacter
from quest.models import Quest

register = template.Library()

@register.simple_tag
def guild_summary_counts():
    """Returns a dictionary of live campaign metrics for any template."""
    return {
        'living_heroes': PlayerCharacter.objects.filter(alive=True).count(),
        'fallen_heroes': PlayerCharacter.objects.filter(alive=False).count(),
        'open_quests': Quest.objects.filter(status='OPEN').count(),
    }
