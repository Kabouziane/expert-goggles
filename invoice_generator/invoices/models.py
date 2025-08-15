from django.db import models
from django.utils import timezone

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    adresse = models.TextField()
    
    def __str__(self):
        return self.nom

class Facture(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=timezone.now)
    date_echeance = models.DateField()
    description = models.TextField()
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2)
    taux_tva = models.DecimalField(max_digits=5, decimal_places=2, default=20.00)
    
    @property
    def montant_tva(self):
        return self.montant_ht * self.taux_tva / 100
    
    @property
    def montant_ttc(self):
        return self.montant_ht + self.montant_tva
    
    def __str__(self):
        return f"Facture {self.numero}"