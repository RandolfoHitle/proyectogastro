from django.urls import path
from .views import  HomeViewPrivate 

urlpatterns = [
     path('', HomeViewPrivate.as_view(), name='homePrivate'),

]
