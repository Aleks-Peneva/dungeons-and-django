from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render

from character.forms import PlayerCharacterCreateForm, PlayerCharacterUpdateForm, InventoryItemForm
from character.models import PlayerCharacter, InventoryItem
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# test view
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('These are your PCs.')

class CharacterListView(ListView):
    model = PlayerCharacter
    template_name = 'character/list.html'
    context_object_name = 'characters'

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        sort = self.request.GET.get('sort')

        if status == 'alive':
            queryset = queryset.filter(alive=True)
        elif status == 'fallen':
            queryset = queryset.filter(alive=False)

        if sort == 'level_asc':
            queryset = queryset.order_by('level', 'name')
        elif sort == 'name':
            queryset = queryset.order_by('name')

        return queryset

class CharacterDetailView(DetailView):
    model = PlayerCharacter
    template_name = 'character/detail.html'

class CharacterCreateView(CreateView):
    model = PlayerCharacter
    form_class = PlayerCharacterCreateForm
    template_name = 'character/playercharacter_form.html'

class CharacterUpdateView(UpdateView):
    model = PlayerCharacter
    form_class = PlayerCharacterUpdateForm
    template_name = 'character/playercharacter_form.html'

class CharacterDeleteView(DeleteView):
    model = PlayerCharacter
    template_name = 'character/confirm_delete.html'
    success_url = reverse_lazy('character:list')


class ItemListView(ListView):
    model = InventoryItem
    template_name = 'character/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('character')
        attuned = self.request.GET.get('attuned')

        if attuned == 'yes':
            queryset = queryset.filter(is_attuned=True)

        return queryset


class ItemCreateView(CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'character/item_form.html'

    def get_initial(self):
        initial = super().get_initial()
        char_id = self.request.GET.get('character')
        if char_id:
            initial['character'] = char_id
        return initial


class ItemUpdateView(UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'character/item_form.html'


class ItemDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'character/item_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('character:detail', kwargs={'pk': self.object.character.pk})
