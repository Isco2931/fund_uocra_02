from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'usuario/registro.html'
    success_url = 'index'