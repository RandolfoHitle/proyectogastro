from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Categoria, Receta

# Listar Categorias
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/categoria_list.html'
    context_object_name = 'categorias'

# Crear Categoria
class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria-list')

# Editar Categoria
class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria-list')

# Eliminar Categoria
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria-list')


# Listar Recetas
class RecetaListView(ListView):
    model = Receta
    template_name = 'receta/receta_list.html'
    context_object_name = 'recetas'

# Detalle de Receta
class RecetaDetailView(DetailView):
    model = Receta
    template_name = 'receta/receta_detail.html'
    context_object_name = 'receta'

# Crear Receta
class RecetaCreateView(CreateView):
    model = Receta
    fields = ['titulo', 'ingredientes', 'instrucciones', 'tiempo_preparacion', 'categoria', 'imagen', 'autor', 'valoracion']
    template_name = 'receta/receta_form.html'
    success_url = reverse_lazy('receta-list')

# Editar Receta
class RecetaUpdateView(UpdateView):
    model = Receta
    fields = ['titulo', 'ingredientes', 'instrucciones', 'tiempo_preparacion', 'categoria', 'imagen', 'autor', 'valoracion']
    template_name = 'receta/receta_form.html'
    success_url = reverse_lazy('receta-list')

# Eliminar Receta
class RecetaDeleteView(DeleteView):
    model = Receta
    template_name = 'receta/receta_confirm_delete.html'
    success_url = reverse_lazy('receta-list')