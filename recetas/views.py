from django.shortcuts import render, get_object_or_404
from .models import Receta

# Parte pública pruebas
def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'recetas/detalle_receta.html', {'receta': receta})
# Parte pública final
def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})

# Parte privada (requiere autenticación)
from django.contrib.auth.decorators import login_required

@login_required
def gestion_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/gestion_recetas.html', {'recetas': recetas})
