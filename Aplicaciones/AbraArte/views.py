from django.shortcuts import render
from .models import ObraArte
from django.contrib import messages

# Create your views here.
def inicioArte(request):
    listadoArte = ObraArte.objects.all()
    return render(request, 'inicioArte.html', {'listadoArte': listadoArte})
