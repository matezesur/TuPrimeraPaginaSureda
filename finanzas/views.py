from django.shortcuts import render, redirect
from .forms import (
    ArticuloFinancieroForm,
    ServicioFinancieroForm,
    ConsultaClienteForm,
    BusquedaArticuloForm,
)
from .models import ArticuloFinanciero, ServicioFinanciero, ConsultaCliente


def inicio(request):
    articulos = ArticuloFinanciero.objects.all().order_by('-fecha_publicacion')[:3]
    servicios = ServicioFinanciero.objects.all()[:3]
    contexto = {
        'articulos': articulos,
        'servicios': servicios,
    }
    return render(request, 'finanzas/inicio.html', contexto)


def lista_articulos(request):
    articulos = ArticuloFinanciero.objects.all().order_by('-fecha_publicacion')
    return render(request, 'finanzas/lista_articulos.html', {'articulos': articulos})


def crear_articulo(request):
    if request.method == 'POST':
        formulario = ArticuloFinancieroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_articulos')
    else:
        formulario = ArticuloFinancieroForm()

    return render(request, 'finanzas/crear_articulo.html', {'formulario': formulario})


def lista_servicios(request):
    servicios = ServicioFinanciero.objects.all()
    return render(request, 'finanzas/lista_servicios.html', {'servicios': servicios})


def crear_servicio(request):
    if request.method == 'POST':
        formulario = ServicioFinancieroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_servicios')
    else:
        formulario = ServicioFinancieroForm()

    return render(request, 'finanzas/crear_servicio.html', {'formulario': formulario})


def lista_consultas(request):
    consultas = ConsultaCliente.objects.all().order_by('-fecha_consulta')
    return render(request, 'finanzas/lista_consultas.html', {'consultas': consultas})


def crear_consulta(request):
    if request.method == 'POST':
        formulario = ConsultaClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_consultas')
    else:
        formulario = ConsultaClienteForm()

    return render(request, 'finanzas/crear_consulta.html', {'formulario': formulario})


def buscar_articulos(request):
    formulario = BusquedaArticuloForm(request.GET)
    resultados = []
    busqueda = ''

    if formulario.is_valid():
        busqueda = formulario.cleaned_data.get('busqueda')
        if busqueda:
            resultados = ArticuloFinanciero.objects.filter(titulo__icontains=busqueda)

    contexto = {
        'formulario': formulario,
        'resultados': resultados,
        'busqueda': busqueda,
    }
    return render(request, 'finanzas/buscar_articulos.html', contexto)
