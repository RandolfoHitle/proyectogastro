from django.urls import path
from .views import LoginFormView, UserRegisterView, LogoutView

urlpatterns = [
     path('login/', LoginFormView.as_view(), name='login'),
     path('register/', UserRegisterView.as_view(), name='register'),
     path('logout/', LogoutView.as_view(), name='logout'),

]
