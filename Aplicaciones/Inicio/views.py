from django.shortcuts import render

def indexMuseo(request):
    return render(request, "Inicio/indexMuseo.html")
