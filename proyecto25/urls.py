"""proyecto25 URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicaciones.Inicio.urls')), 
    path('ObraArte/', include('Aplicaciones.AbraArte.urls')),
    path('Exposicion/', include('Aplicaciones.Exposicion.urls')),
    path('Reserva/', include('Aplicaciones.Reserva.urls')),
    path('Visitante/', include('Aplicaciones.Visitante.urls')),
    path('Generos/', include('Aplicaciones.Genero.urls')),
    path('Peliculas/', include('Aplicaciones.Pelicula.urls')),
    path('Tipo/', include('Aplicaciones.Tipo.urls')),
    path('Artista/', include('Aplicaciones.Artista.urls')),

]
