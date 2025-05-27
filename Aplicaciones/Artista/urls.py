from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarArtistas, name='listarArtistas'),  
    path('nuevoArtista/', views.nuevoArtista, name='nuevoArtista'),  
    path('guardarArtista/', views.guardarArtista, name='guardarArtista'),  
    path('eliminarArtista/<id>/', views.eliminarArtista),  
    path('editarArtista/<id>/', views.editarArtista, name='editarArtista'),  
    path('procesarEdicionArtista/<id>/', views.procesarEdicionArtista, name='procesarEdicionArtista'),  
]
