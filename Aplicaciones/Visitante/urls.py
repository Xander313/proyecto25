from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioVisitante, name='indexVisitante'),  
    path('nuevoVisitante', views.nuevoVisitante, name='nuevoVisitante'),  
    path('guardarVisitante', views.guardarVisitante, name='guardarVisitante'),  
    path('eliminarVisitante/<id>', views.eliminarVisitante),  
    path('editarVisitante/<id>', views.editarVisitante, name='editarVisitante'),  
    path('procesarEdicionVisitante/<id>', views.procesarEdicionVisitante, name='procesarEdicionVisitante'),  
]
