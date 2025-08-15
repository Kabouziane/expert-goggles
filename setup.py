import os
import django
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invoice_generator.settings')
django.setup()

# Créer les migrations et la base de données
execute_from_command_line(['manage.py', 'makemigrations'])
execute_from_command_line(['manage.py', 'migrate'])

# Créer un superutilisateur (optionnel)
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superutilisateur créé: admin/admin123")

# Créer des données de test
from invoice_generator.invoices.models import Client, Facture
from datetime import date, timedelta

if not Client.objects.exists():
    client = Client.objects.create(
        nom="Entreprise ABC",
        email="contact@abc.com",
        adresse="123 Rue de la Paix, 75001 Paris"
    )
    
    Facture.objects.create(
        numero="F001",
        client=client,
        date_echeance=date.today() + timedelta(days=30),
        description="Prestation de développement web",
        montant_ht=1000.00
    )
    print("Données de test créées")