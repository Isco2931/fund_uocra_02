from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
#LEER SOBRE VISTAS BASADAS EN CLASES Y VISTAS GENERICAS
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Noticia, Categoria
# Create your views here.

#    min 15:24
#
class AddNoticia(CreateView):
    model = Noticia
    fields = ['titulo', 'texto', 'categoria', 'imagen']
    template_name = 'noticia/addNoticia.html'
    success_url = reverse_lazy('index')
class AddCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'noticia/addCategoria.html'
    success_url = reverse_lazy('index')

"""
Es otra forma de definir la vista mostrar noticia
class MostrarNoticia(ListView):
    model = Noticia
    template_name = '/noticia/mostrarNoticia.html'
    el template de esta clase explica en el video 18 min 17
    si quiero filtrar debo usar:
    def get_queryset(self):
"""
def ListarNoticia (request):
    noticia = Noticia.objects.all()
    context = {
        'noticia': noticia,
    }
    return render(request, 'noticia/listarNoticia.html', context)

def ListarNoticiaPorCategoria (request, categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia = Noticia.objects.filter(categoria=categoria2[0].id)
    context = {
        'noticia': noticia,
    }
    return render(request, 'category.html', context)
"""
class ListarCategoria(ListView):
    model = Categoria
    template_name = 'noticia/listarCategoria.html'

def ListarCategoria (request):
    categoria = Categoria.objects.all()
    context = {
        'categoria': categoria,
    }
    return render(request, 'noticia/listarCategoria.html', context)
"""
