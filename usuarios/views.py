from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import NuestroFormularioDeCreacion


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
        
            user = authenticate(request, username=usuario, password=contrasenia)

            django_login(request, user)

            return redirect('inicio')
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    
    formulario = NuestroFormularioDeCreacion()
    
    if request.method == "POST":
        formulario = NuestroFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    return render(request, 'usuarios/registro.html', {'formulario': formulario})