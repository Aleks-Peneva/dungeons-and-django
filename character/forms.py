from django import forms
from django.core.exceptions import ValidationError
from .models import PlayerCharacter, InventoryItem

class PlayerCharacterCreateForm(forms.ModelForm):
    class Meta:
        model = PlayerCharacter
        fields = '__all__'
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
        'player_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Alex'}),
        'character_class': forms.Select(attrs={'class': 'form-select'}),
        'character_race': forms.Select(attrs={'class': 'form-select'}),
        'level': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20}),
        'alive': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'notes': forms.Textarea(
            attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Backstory, bonds, or guild reputation...'}),
    }


class PlayerCharacterUpdateForm(PlayerCharacterCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['name'].help_text = 'Character names cannot be modified'
        # could renaming a character be valid, e.g. when adding titles? to review


class InventoryItemForm(forms.ModelForm):
    # used to track if players go over their max 3 items attuned limit
    class Meta:
        model = InventoryItem
        fields = '__all__'
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

        def clean(self):
            cleaned_data = super().clean()
            character = cleaned_data.get('character')
            is_attuned = cleaned_data.get('is_attuned')
            requires_attunement = cleaned_data.get('requires_attunement')

            if is_attuned and not requires_attunement:
                self.add_error(
                    'is_attuned',
                    "This item does not require attunement, so you can't attune it."
                )

            if character and is_attuned and not requires_attunement:
                attuned_items = character.inventory.filter(is_attuned=True)
                if self.instance.pk:
                    attuned_items = attuned_items.exclude(pk=self.instance.pk)
                if attuned_items.count() >= 3:
                    raise ValidationError(
                        f"{character.name} is already attuned to 3 magic items, they need to unattune from one of them first."
                    )
            return cleaned_data