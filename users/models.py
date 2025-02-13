from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('creator', 'creador'),
        ('admin', 'Administrador'),
    )
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='creator')