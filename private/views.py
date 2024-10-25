from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeViewPrivate(TemplateView):
    template_name =  'dashboard.html'