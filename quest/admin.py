from django.contrib import admin
from .models import Quest


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'summary', 'status', 'awarding_XP')
    list_filter = ('status',)
    search_fields = ('title', 'location', 'summary')
    filter_horizontal = ('involved_characters',)
