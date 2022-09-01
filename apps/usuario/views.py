from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Usuario
from .forms import RegistroUsuarioFrom

class RegistrarUsuario(CreateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/registro.html'
#   success_url = reverse_lazy('login')

