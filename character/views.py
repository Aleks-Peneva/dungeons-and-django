from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from character.forms import PlayerCharacterCreateForm, PlayerCharacterUpdateForm
from character.models import PlayerCharacter
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
        alive = self.request.GET.get('alive')
        # TODO: maybe sorting

        if alive == 'true':
            queryset = queryset.filter(alive=True)
        elif alive == 'false':
            queryset = queryset.filter(alive=False)

        return queryset

class CharacterDetailView(DetailView):
    model = PlayerCharacter
    template_name = 'character/detail.html'

class CharacterCreateView(CreateView):
    model = PlayerCharacter
    form_class = PlayerCharacterCreateForm

class CharacterUpdateView(UpdateView):
    model = PlayerCharacter
    form_class = PlayerCharacterUpdateForm
