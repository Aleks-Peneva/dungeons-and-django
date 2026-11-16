from django import forms
from .models import PlayerCharacter, InventoryItem

class PlayerCharacterCreateForm(forms.ModelForm):
    class Meta:
        model = PlayerCharacter
        labels = {
            'name': 'Character Name',
            'player_name': 'Player Name',
            'character_class': 'Class',
            'character_race': 'Race',
            'alive': 'Currently Alive',
        }
    help_texts = {
        'level': 'You can level up from level one and reach nigh godhood at level 20.',
    }
    error_messages = {
        'name': {
            'unique': 'To avoid confusion at the table, character names must be unique',
        },
    }
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        # TODO: add the rest after testing
    }


class PlayerCharacterUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['name'].help_text = 'Character names cannot be modified'
        # although renaming a character could be valid, e.g. when adding titles, to review

class InventoryItemForm(forms.ModelForm):
    # used to track if players go over their max 3 items attuned limit
    class Meta:
        model = InventoryItem
        fields = ['name', 'character', 'quantity', 'requires_attunement', 'is_attuned']
        labels = {
            'requires_attunement': 'This item require attunement (max 3 items attuned at a time)',
            'is_attuned': 'This item is currently attuned',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'character': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'requires_attunement': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_attuned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Item properties,charges, damage...'}),
        }