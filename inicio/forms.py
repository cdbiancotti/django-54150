from django import forms

class CrearAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    anio = forms.IntegerField()