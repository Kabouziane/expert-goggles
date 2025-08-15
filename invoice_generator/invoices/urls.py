from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_factures, name='liste_factures'),
    path('creer/', views.creer_facture, name='creer_facture'),
    path('facture/<int:pk>/', views.detail_facture, name='detail_facture'),
    path('facture/<int:pk>/pdf/', views.generer_pdf, name='generer_pdf'),
]