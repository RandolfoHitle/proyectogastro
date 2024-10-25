from django.urls import path
from .views import HomeViewPublic, RecetasViewPublic, ContactoViewPublic, HistoriaViewPublic, RecetaDetailViewPublic

urlpatterns = [
    path('', HomeViewPublic.as_view(), name='homePublic'),
    path('recetario/', RecetasViewPublic.as_view(), name='recetasPublic'),
    path('recetario/<int:pk>/', RecetaDetailViewPublic.as_view(), name='receta_detailPublic'),
    path('contacto/', ContactoViewPublic.as_view(), name='contactoPublic'),
    path('historia/', HistoriaViewPublic.as_view(), name='historiaPublic'),

]
