from django.urls import path
from character.views import index

urlpatterns = [
    path('', index, name='index'),
    # TODO: CRUD views for characters and inventory items
]
