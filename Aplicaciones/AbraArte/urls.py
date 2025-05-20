from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioArte),  
    path('nuevoArte', views.nuevaArte),  
    path('guardarArte', views.guardarArte),  
    path('eliminarArte/<id>', views.eliminarArte),  
    path('editarArte/<id>', views.editarArte),  
    path('procesarEdicionArte', views.procesarEdicionArte), 
]
