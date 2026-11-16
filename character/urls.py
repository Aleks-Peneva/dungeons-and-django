from django.urls import path
from character.views import index, characters_list

urlpatterns = [
    path('', index, name='index'),
    path('character/', characters_list, name='list'),
    # TODO: CRUD views for characters and inventory items
]
