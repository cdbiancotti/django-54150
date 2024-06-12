from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('template1/<str:nombre>/<str:apellido>/<int:edad>', views.template1),
    path('template2/<str:nombre>/<str:apellido>/<int:edad>', views.template2),
    path('template3/<str:nombre>/<str:apellido>/<int:edad>', views.template3),
    path('template4/<str:nombre>/<str:apellido>/<int:edad>', views.template4),
    path('prueba/', views.probando, name="probando"),
    path('autos/', views.autos, name='autos'),
    # V1
    # path('autos/crear/<str:marca>/<str:modelo>/', views.crear_auto, name='crear_auto'),
    # V2
    path('autos/crear/', views.crear_auto_v2, name='crear_auto_v2'),
    path('autos/eliminar/<int:id>/', views.eliminar_auto, name='eliminar_auto'),
    path('autos/editar/<int:id>/', views.editar_auto, name='editar_auto'),
    path('autos/<int:id>/', views.ver_auto, name='ver_auto'),
]
