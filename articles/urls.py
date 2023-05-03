from django.urls import path
from .views import liste_articles

urlpatterns = [
    path('', liste_articles, name='liste_articles'),
]
