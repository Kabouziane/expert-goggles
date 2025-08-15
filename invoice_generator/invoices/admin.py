from django.contrib import admin
from .models import Client, Facture

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email']

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ['numero', 'client', 'date_creation', 'montant_ttc']
    list_filter = ['date_creation']