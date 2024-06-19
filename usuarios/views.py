from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import NuestroFormularioDeCreacion, EditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
        
            user = authenticate(request, username=usuario, password=contrasenia)

            django_login(request, user)

            DatosExtra.objects.get_or_create(user=user)

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

@login_required
def editar_perfil(request):
    
    datosextra = request.user.datosextra
    formulario = EditarPerfil(initial={'avatar': datosextra.avatar}, instance=request.user)
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, request.FILES , instance=request.user)
        if formulario.is_valid():
            
            
            datosextra.avatar = formulario.cleaned_data.get('avatar')
            datosextra.save()
            
            formulario.save()
            return redirect('editar_perfil')
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_pass.html'
    success_url = reverse_lazy('editar_perfil')