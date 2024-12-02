from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, RegistroForm
from .models import Cliente
#Para reportes
# instalar reportlab
# pip install reportlab
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q




# Create your views here.
@login_required
def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})
    
def cliente_list(request):
    query = request.GET.get("q")
    if query:
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) | Q(apellidos__icontains = query)
        )
    else: 
        clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

@login_required
def update_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_form.html', {'form': form, 'cliente': cliente})

@login_required
def delete_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method =='POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})

# Reportes
def generar_pdf_cliente(request):
    response = HttpResponse(content_type='application/pdf')
    # abrir = inline, descargar = attachment
    response['Content-Disposition'] = 'inline; filename="clientes.pdf"'

    pdf = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    pdf.setTitle("Reporte de Clientes")
    fecha_generacion = datetime.date.today().strftime("%d-%m-%Y")
    pagina_num = 1

    def pie_pagina(pdf, pagina_num):
        pdf.setFont("Helvetica", 10)
        pdf.drawString(50, 20, f"Fecha de generación: {fecha_generacion}")
        pdf.drawString(width - 100, 20, f"Página núm. {pagina_num}")

    # Título del reporte centrado
    pdf.setFont("Helvetica-Bold", 16)
    texto = "Lista de Clientes"
    ancho_texto = pdf.stringWidth(texto)
    x = (width - ancho_texto) / 2
    pdf.drawString(x, height - 40, texto)

    # Encabezados de la tabla del mismo ancho
    encabezados = ["Nombre", "Apellidos", "Fecha de nac."]
    x_inicial = 100
    y = height - 80 
    pdf.setFont("Helvetica-Bold", 12)
    for i, encabezado in enumerate(encabezados):
        pdf.drawString(x_inicial + i * 150, y , encabezado)

    y -= 10
    pdf.line(100, y, width-100, y)

    y -= 20
    query = request.GET.get("q")
    if query:
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) | Q(apellidos__icontains = query)
        )
    else: 
        clientes = Cliente.objects.all()
    pdf.setFont("Helvetica", 12)
    for cliente in clientes:
        pdf.drawString(100, y , cliente.nombre)
        pdf.drawString(250, y , cliente.apellidos)
        pdf.drawString(400, y , cliente.fecha_nac.strftime("%d-%m-%Y"))
        y -= 20

        if y <= 50:
            pie_pagina(pdf, pagina_num)
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            

            y = height - 80             
            for i, encabezado in enumerate(encabezados):
                pdf.drawString(x_inicial + i * 150, y , encabezado)
            y -= 10
            pdf.line(100, y, width-100, y)
            y -= 20

            pagina_num += 1



    pie_pagina(pdf, pagina_num)




    pdf.showPage()
    pdf.save()

    return response

def logout_view(request):
    logout(request)
    return redirect('login')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})