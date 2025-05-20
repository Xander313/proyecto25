from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioPelicula, name='indexPelicula'),  
    path('nuevoPelicula', views.nuevaPelicula, name='Pelicula'),  
    #path('guardarPelicula', views.guardarPelicula, name='guardarPelicula'),  
    path('eliminarPelicula/<id>', views.eliminarPelicula),  
    path('editarPelicula/<id>', views.editarPelicula, name='editarPelicula'),  
    path('procesarEdicionPelicula/<id>', views.procesarEdicionPelicula, name='procesarEdicionPelicula'), 
]
