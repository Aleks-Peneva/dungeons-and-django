from django import template
from character.models import PlayerCharacter
from quest.models import Quest

register = template.Library()

@register.filter(name='level-tier')
def level_tier(level):
    try:
        lvl = int(level)
        if lvl <= 4:
            return "Local Heroes"
        elif lvl <= 10:
            return "Heroes of the Realm"
        elif lvl <= 16:
            return "Masters of the Realm"
        else:
            return "Masters of the World"
    except (ValueError, TypeError):
        return "Outside of official Tiers of Play"

@register.simple_tag
def guild_summary_counts():
    return {
        'living_heroes': PlayerCharacter.objects.filter(alive=True).count(),
        'fallen_heroes': PlayerCharacter.objects.filter(alive=False).count(),
        'open_quests': Quest.objects.filter(status='DISCOVERED').count(),
    }
