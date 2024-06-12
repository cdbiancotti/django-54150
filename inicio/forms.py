from django import forms

class AutoFormularioBase(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    
class CrearAutoFormulario(AutoFormularioBase):
    ...
    
class EditarAutoFormulario(AutoFormularioBase):
    ...
    
class BuscarAuto(forms.Form):
    marca = forms.CharField(max_length=20, required=False)