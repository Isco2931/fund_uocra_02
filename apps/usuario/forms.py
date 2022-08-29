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