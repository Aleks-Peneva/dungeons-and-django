from django.urls import path
from . import views

app_name = 'quest'
urlpatterns = [
    path('', views.QuestListView.as_view(), name='list'),
    path('new/', views.QuestCreateView.as_view(), name='create'),
    path('<int:pk>/', views.QuestDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.QuestUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.QuestDeleteView.as_view(), name='delete'),
]