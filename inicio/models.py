from django.db import models

class Auto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    anio = models.IntegerField(default=2010)
    
    def __str__(self):
        return f'Soy el auto {self.modelo} {self.marca}'