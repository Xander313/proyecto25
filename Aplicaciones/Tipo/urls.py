from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarTipos, name='listarTipos'),  
    path('nuevoTipo/', views.nuevoTipo, name='nuevoTipo'),  
    path('guardarTipo/', views.guardarTipo, name='guardarTipo'),  
    path('eliminarTipo/<id>/', views.eliminarTipo),  
    path('editarTipo/<id>/', views.editarTipo, name='editarTipo'),  
    path('procesarEdicionTipo/<id>/', views.procesarEdicionTipo, name='procesarEdicionTipo'),  
]
