from django import forms
from .models import Promotion

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ('pourcentage', 'date_debut', 'date_fin')
