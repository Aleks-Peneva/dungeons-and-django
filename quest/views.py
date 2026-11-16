from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quest
from .forms import QuestForm

class QuestListView(ListView):
    model = Quest
    template_name = 'quest/list.html'
    context_object_name = 'quests'

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('involved_characters')
        status = self.request.GET.get('status')
        sort = self.request.GET.get('sort')

        valid_statuses = {'UNDISCOVERED', 'DISCOVERED', 'IN_PROGRESS', 'COMPLETED', 'FAILED'}
        if status in valid_statuses:
            queryset = queryset.filter(status=status)

        if sort == 'xp_asc':
            queryset = queryset.order_by('awarding_XP', '-created_at')
        elif sort == 'xp_desc':
            queryset = queryset.order_by('-awarding_XP', '-created_at')

        return queryset


class QuestDetailView(DetailView):
    model = Quest
    template_name = 'quest/detail.html'


class QuestCreateView(CreateView):
    model = Quest
    form_class = QuestForm
    template_name = 'quest/quest_form.html'


class QuestUpdateView(UpdateView):
    model = Quest
    form_class = QuestForm
    template_name = 'quest/quest_form.html'


class QuestDeleteView(DeleteView):
    model = Quest
    template_name = 'quest/quest_confirm_delete.html'
    success_url = reverse_lazy('quest:list')