from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexReserva, name='indexReserva'),  
    path('nuevaReserva/', views.nuevaReserva, name='nuevaReserva'),  
    path('guardarReserva', views.guardarReserva, name='guardarReserva'),  
    path('eliminarReserva/<id>', views.eliminarReserva),  
    path('editarReserva/<id>', views.editarReserva, name='editarReserva'),  
    path('procesarEdicionReserva/<id>', views.procesarEdicionReserva, name='procesarEdicionReserva'), 
]
