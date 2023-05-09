from django.urls import path
from .views import add_promotion

app_name = 'promotion'

urlpatterns = [
   path('add_promotion/<int:article_id>/', add_promotion, name='add_promotion'),
]
