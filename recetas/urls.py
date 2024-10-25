from django.urls import path
from .views import (
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,
    RecetaListView, RecetaCreateView, RecetaUpdateView, RecetaDeleteView, RecetaDetailView
)


urlpatterns = [
    # URLs para Categorias
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/nueva/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('categorias/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categorias/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria-delete'),
    
    # URLs para Recetas
    path('recetas/', RecetaListView.as_view(), name='receta-list'),
    path('recetas/nueva/', RecetaCreateView.as_view(), name='receta-create'),
    path('recetas/editar/<int:pk>/', RecetaUpdateView.as_view(), name='receta-update'),
    path('recetas/eliminar/<int:pk>/', RecetaDeleteView.as_view(), name='receta-delete'),
    path('recetas/<int:pk>/', RecetaDetailView.as_view(), name='receta-detail'),
]
