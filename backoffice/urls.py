from django.urls import path
from .views import ajouter_article

urlpatterns = [
    path('ajouter-article/', ajouter_article, name='ajouter_article'),
]
