from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicioExposicion, name='indexExposicion'),  
    path('nuevaExposicion', views.nuevaExposicion, name='nuevaExposicion'),  
    path('guardarExposicion', views.guardarExposicion, name='guardarExposicion'),  
    path('eliminarExposicion/<id>', views.eliminarExposicion),  
    path('editarExposicion/<id>', views.editarExposicion, name='editarExposicion'),  
    path('procesarEdicionExposicion/<id>', views.procesarEdicionExposicion, name='procesarEdicionExposicion'),  
]

