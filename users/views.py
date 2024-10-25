from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from authentication.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User

User = get_user_model()

# Lista de usuarios
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

# Crear usuario
class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/user_formCreate.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuario creado exitosamente.')
        return super().form_valid(form)

# Editar usuario
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'photo', 'role']
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuario actualizado exitosamente.')
        return super().form_valid(form)

# Eliminar usuario
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Usuario eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
