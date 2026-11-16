from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='list'),
    path('new/', views.CharacterCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.CharacterUpdateView.as_view(), name='update'),
    # TODO: finish CRUD views for characters and inventory items
]
