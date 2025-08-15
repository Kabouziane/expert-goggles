from django import forms
from .models import Facture, Client

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['numero', 'client', 'date_echeance', 'description', 'montant_ht', 'taux_tva']
        widgets = {
            'date_echeance': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }