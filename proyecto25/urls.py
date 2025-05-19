"""proyecto25 URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AbraArte/', include('Aplicaciones.AbraArte.urls')),
    path('Exposicion/', include('Aplicaciones.Exposicion.urls')),
    path('Reserva/', include('Aplicaciones.Reserva.urls')),
    path('Visitante/', include('Aplicaciones.Visitante.urls')),
]
