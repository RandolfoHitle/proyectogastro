from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_recetas, name='lista_recetas'),  # Lista de recetas públicas
    path('receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),  # Detalle de receta
    path('gestion/', views.gestion_recetas, name='gestion_recetas'),  # Vista de gestión privada
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.lista_recetas, name='lista_recetas'),
    path('', views.lista_recetas, name='home'),
]