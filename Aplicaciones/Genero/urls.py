from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioGenero, name='indexGenero'),  
    path('nuevoGenero/', views.nuevaGenero, name='Genero'),  
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),  
    path('eliminarGenero/<id>', views.eliminarGenero),  
    path('editarGenero/<id>', views.editarGenero, name='editarGenero'),  
    path('procesarEdicionGenero/<id>', views.procesarEdicionGenero, name='procesarEdicionGenero'), 
]
