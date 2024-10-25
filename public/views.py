from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from recetas.models import Receta, Categoria

class HomeViewPublic(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener las últimas 3 recetas, o menos si no hay suficientes
        context['ultimas_recetas'] = Receta.objects.order_by('-fecha_creacion')[:3]
        return context

class RecetasViewPublic(ListView):
    model = Receta
    template_name = 'recetario.html'
    context_object_name = 'recetas'

    def get_queryset(self):
        # Obtiene todas las recetas
        queryset = super().get_queryset()
        # Filtrar por nombre
        nombre = self.request.GET.get('nombre')
        if nombre:
            queryset = queryset.filter(titulo__icontains=nombre)

        # Filtrar por categoría
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categoria__id=categoria_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  # Pasar todas las categorías al contexto
        return context
    
class RecetaDetailViewPublic(DetailView):
    model = Receta
    template_name = 'recetario_detail.html'  # Crea este archivo en tu carpeta de templates
    context_object_name = 'receta'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  # Pasar todas las categorías al contexto
        return context

class HistoriaViewPublic(TemplateView):
    template_name =  'historia.html'

class ContactoViewPublic(TemplateView):
    template_name =  'contacto.html'