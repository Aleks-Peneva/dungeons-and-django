from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'campaign_manager'
urlpatterns = [
    path('', views.DMScreenView.as_view(), name='dmscreen'),
    path('rules/', views.AboutDMScreenView.as_view(), name='about'),
    path('404-preview/', TemplateView.as_view(template_name='404.html'), name='404-preview'),
]