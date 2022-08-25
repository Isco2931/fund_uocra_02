"""from django.shortcuts import render
from django.views.generic.edit import CreateView
#from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from .models import Usuario
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

User = get_user_model()

class UserRegisterView(CreateView):
    model= Usuario
    form_class = UserCreationForm
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('login')
    class Meta:
        model = get_user_model()

class UserRegisterView(CreateView):
    model = Usuario
    fields = ['first_name', 'last_name', 'username', 'email', 'password']
#    password = make_password(Usuario.password)
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('login')
    """
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Usuario
from .forms import RegistroUsuarioFrom

""" from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = Usuario
		#fields = UserCreationForm.Meta.fields + ('imagen')
		template_name = 'usuario/registrar.html' """

class RegistrarUsuario(CreateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/registro.html'
#    success_url = reverse_lazy('login')

"""
class ModificarUsuario(UpdateView):
	model = Usuario
	form_class = RegistroUsuarioFrom
	template_name = 'usuario/modificar.html'

class DeleteUsuario(DeleteView):
	model = Usuario
	success_url = reverse_lazy('index')
    """