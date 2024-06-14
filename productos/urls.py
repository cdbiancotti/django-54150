from django.urls import path
from . import views

urlpatterns = [
    path('paletas/', views.Paletas.as_view(), name='paletas'),
    path('paletas/crear/', views.CrearPaleta.as_view(), name='crear_paleta'),
    path('paletas/<int:pk>/', views.VerPaleta.as_view(), name='ver_paleta'),
    path('paletas/<int:pk>/editar/', views.EditarPaleta.as_view(), name='editar_paleta'),
    path('paletas/<int:pk>/eliminar/', views.EliminarPaleta.as_view(), name='eliminar_paleta'),
]
