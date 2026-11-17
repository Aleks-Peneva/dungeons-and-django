from django.contrib import admin
from .models import PlayerCharacter, InventoryItem
#
# class InventoryItemInline(admin.TabularInline):
#     model = InventoryItem
#     extra = 1
#
# @admin.register(PlayerCharacter)
# class CharacterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'character_class', 'character_race', 'level', 'player_name')
#     list_filter = ('character_class', 'character_race')
#     search_fields = ('name', 'player_name')
#     inlines = [InventoryItemInline]
#
#
# @admin.register(InventoryItem)
# class InventoryItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'character', 'quantity', 'requires_attunement', 'is_attuned')
#     list_filter = ('is_attuned', 'character')
#     search_fields = ('name', 'description')