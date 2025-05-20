from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioArte, name='indexArte'),  
    path('nuevoArte', views.nuevaArte, name='obraArte'),  
    path('guardarArte', views.guardarArte, name='guardarArte'),  
    path('eliminarArte/<id>', views.eliminarArte),  
    path('editarArte/<id>', views.editarArte, name='editarArte'),  
    path('procesarEdicionArte/<id>', views.procesarEdicionArte, name='procesarEdicionArte'), 
]
