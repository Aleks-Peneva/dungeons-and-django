from django.urls import path
from . import views

app_name = 'character'
urlpatterns = [
    path('', views.CharacterListView.as_view(), name='list'),
    path('new/', views.CharacterCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CharacterDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.CharacterUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.CharacterDeleteView.as_view(), name='delete'),

    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('items/new/', views.ItemCreateView.as_view(), name='item-create'),
    path('items/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item-delete'),
]
