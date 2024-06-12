from django.shortcuts import render, redirect
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from inicio.models import Auto
# from .models import Auto
from inicio.forms import CrearAutoFormulario, BuscarAuto, EditarAutoFormulario

import random

def inicio(request):
    # v1
    # return HttpResponse('Bienvenidos a mi INICIO!!')
    return render(request, 'inicio/index.html')

def template1(request, nombre, apellido, edad):
    fecha = datetime.now()
    suma = 4 + edad
    
    return HttpResponse(f'<h1>Mi Template 1</h1> -- Fecha: {fecha} -- Buenas {nombre} {apellido} {edad}')

def template2(request, nombre, apellido, edad):
    
    archivo_abierto = open(r'C:\Users\cdbia\Desktop\programacion\mi-proyecto\templates\template2.html')
    # archivo_abierto = open('templates\template2.html')
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellid': apellido,
        'edad': edad,
        }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)


def template3(request, nombre, apellido, edad):
    
    template = loader.get_template('template2.html')
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellid': apellido,
        'edad': edad,
        }
    
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)


def template4(request, nombre, apellido, edad):
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellid': apellido,
        'edad': edad,
        }
    
    return render(request,'template2.html', datos)

def probando(request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    print(numeros)
    return render(request, 'probando_if_for.html', {'numeros': numeros})

def crear_auto(request, marca, modelo):
    auto = Auto(marca=marca, modelo=modelo)
    auto.save()
    return render(request, 'auto_templates/creacion.html', {"auto": auto})

def crear_auto_v2(request):
    
    # v1
    # print('Valor de la request: ', request)
    # print('Valor de GET: ', request.GET)
    # print('Valor de POST: ', request.POST)
    
    # if request.method == 'POST':
    #     auto = Auto(marca=request.POST.get('marca'), modelo=request.POST.get('modelo'))
    #     auto.save()
    
    # return render(request, 'inicio/crear_auto_v2.html')

    # v2
    print('Valor de la request: ', request)
    print('Valor de GET: ', request.GET)
    print('Valor de POST: ', request.POST)
    
    formulario = CrearAutoFormulario()
    
    if request.method == 'POST':
        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            auto = Auto(marca=datos.get('marca'), modelo=datos.get('modelo'))
            auto.save()
            return redirect('autos')

    return render(request, 'inicio/crear_auto_v2.html', {'formulario': formulario})

def autos(request):
    
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
        marca = formulario.cleaned_data['marca']
        autos = Auto.objects.filter(marca__icontains=marca)
    
    # autos = Auto.objects.all()
    
    return render(request, 'inicio/autos.html', {'autos': autos, 'formulario': formulario})
    
def eliminar_auto(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()
    return redirect('autos')
    
def editar_auto(request, id):
    auto = Auto.objects.get(id=id)
    
    formulario = EditarAutoFormulario(initial={'marca': auto.marca, 'modelo': auto.modelo, 'anio': auto.anio})
    
    if request.method == 'POST':
        formulario = EditarAutoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            auto.marca = info['marca']
            auto.modelo = info['modelo']
            auto.anio = info['anio']
            auto.save()
            return redirect('autos')
    
    return render(request, 'inicio/editar_auto.html', {'formulario': formulario, 'auto': auto})
    
def ver_auto(request, id):
    auto = Auto.objects.get(id=id)
    return render(request, 'inicio/ver_auto.html', {'auto': auto})