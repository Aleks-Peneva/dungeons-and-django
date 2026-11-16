from django import forms
from django.core.exceptions import ValidationError
from .models import Quest

class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        exclude = ['-created_at']
        labels = {
            'awarding_XP': 'XP awarded to players',
            'involved_characters': 'Characters on quest'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Wild Sheep Chase'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Tumbleton Forest'}),
            'awarding_XP': forms.NumberInput(attrs={'class': 'form-control', 'min': 1000}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
                                             'placeholder': 'A transmutated sheep leads the party on a wild chase...'}),
            'involved_characters': forms.CheckboxSelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        characters = cleaned_data.get('involved_characters')

        if status == 'IN_PROGRESS' and (not characters or characters.count() == 0):
            raise ValidationError('You cannot complete this quest without any characters')

        if characters:
            dead = [c.name for c in characters if c.alive == False]
            if dead and status in ['DISCOVERED', 'IN_PROGRESS']:
                raise ValidationError(f'Dead characters must be removed from the quest: {', '.join(dead)}')
            return cleaned_data