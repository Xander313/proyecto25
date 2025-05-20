from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexMuseo, name='indexMuseo'),
]
