from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from character.models import PlayerCharacter, InventoryItem
from quest.models import Quest


# test view
# def index(request: HttpRequest) -> HttpResponse:
#     return HttpResponse('This is your DM screen.')

# this page serves as your DM screen - a dashboard aggregating data across all apps
class DMScreenView(TemplateView):
    template_name = 'campaign_manager/dmscreen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['highest_level_characters'] = PlayerCharacter.objects.order_by('-level','name')[:5]
        context['active_quests'] = Quest.objects.filter(status__in=['DISCOVERED', 'IN_PROGRESS'])[:5]
        context['completed_quests_count'] = Quest.objects.filter(status='COMPLETED').count()
        context['total_items_count'] = InventoryItem.objects.count()
        context['recent_loot'] = InventoryItem.objects.select_related('character').order_by('-pk')[:5]

        return context

class AboutDMScreenView(TemplateView):
    template_name = 'campaign_manager/old_about.html'