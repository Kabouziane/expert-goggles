from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Facture, Client
from .forms import FactureForm
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def liste_factures(request):
    factures = Facture.objects.all().order_by('-date_creation')
    return render(request, 'invoices/liste.html', {'factures': factures})

def creer_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_factures')
    else:
        form = FactureForm()
    return render(request, 'invoices/creer.html', {'form': form})

def detail_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'invoices/detail.html', {'facture': facture})

def generer_pdf(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # En-tête
    p.drawString(100, 750, f"FACTURE N° {facture.numero}")
    p.drawString(100, 720, f"Date: {facture.date_creation.strftime('%d/%m/%Y')}")
    p.drawString(100, 700, f"Échéance: {facture.date_echeance.strftime('%d/%m/%Y')}")
    
    # Client
    p.drawString(100, 650, "FACTURÉ À:")
    p.drawString(100, 630, facture.client.nom)
    p.drawString(100, 610, facture.client.email)
    
    # Description
    p.drawString(100, 550, "DESCRIPTION:")
    p.drawString(100, 530, facture.description)
    
    # Montants
    p.drawString(100, 470, f"Montant HT: {facture.montant_ht} €")
    p.drawString(100, 450, f"TVA ({facture.taux_tva}%): {facture.montant_tva} €")
    p.drawString(100, 430, f"Total TTC: {facture.montant_ttc} €")
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="facture_{facture.numero}.pdf"'
    return response