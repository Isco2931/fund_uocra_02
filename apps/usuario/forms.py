#pal registro
"""
from .models import Usuario

class UserRegisterForm(UserCreationForm):
     email = forms.EmailField(label= 'Correo Electrónico', required=True)
     username = forms.CharField(label = 'Nombre de Usuario', required=True)
     password1 = forms.CharField(label = "Contraseña", required=True)
     password2 = forms.CharField(label = "Confirmar Contraseña", required=True)
class Meta:
    model = Usuario
    fields = ['username', 'email', 'password1', 'password2']"""

from .models import Usuario
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistroUsuarioFrom(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['email', 'username','password1','password2', 'imagen']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_staff = False
        user.save()
        return user