from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Noticia, Categoria


class AddNoticia(CreateView):
    model = Noticia
    fields = ['autor', 'titulo', 'texto', 'categoria', 'imagen']
    template_name = 'noticia/addNoticia.html'
    success_url = reverse_lazy('Listar-Noticia')


class AddCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'noticia/addCategoria.html'
    success_url = reverse_lazy('categoria')


def ListarNoticia (request):
    noticia = Noticia.objects.all()
    categoria = Categoria.objects.all()
    context = {
        'noticia': noticia,
        'categoria': categoria,

    }
    return render(request, 'noticia/listarNoticia.html', context)
    
def ListarNoticiaPorCategoria (request, categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia = Noticia.objects.filter(categoria=categoria2[0].id)
    categoria = Categoria.objects.all()
    context = {
        'noticia': noticia,
        'categoria': categoria,
    }
    return render(request, 'noticia/category.html', context)

def ListarCategoria(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'noticia/listarCategoria.html', context)
    

class UpdateNoticia(UpdateView):
    model = Noticia
    fields = ['autor', 'titulo', 'texto', 'categoria', 'imagen']
    template_name = 'noticia/updateNoticia.html'
    success_url = reverse_lazy('Listar-Noticia')


class DeleteNoticia(DeleteView):
    model = Noticia
    template_name = 'noticia/eliminarNoticia.html'
    success_url = reverse_lazy('Listar-Noticia')


class DetailNoticia(DetailView):
    model = Noticia
    template_name = 'noticia/detailNoticia.html'


################# Contexto Categorias  ####################

def MostrarCategorias(request):
    categorias = Categoria.objects.all()
    context = {
        "categorias": categorias,
    }
    return context

def MostrarComentarios(request):
    comentarios = Comentario.objects.all()
    context = {
        "comentarios": comentarios,
    }
    return ( context)


################# Comentarios Gaston ####################

from apps.comentario.models import Comentario
class CreateComentario(CreateView):
    model = Comentario
    template_name = 'comentario/addComentario2.html'
    fields = ['autor','noticia','comentario', ]
    success_url = reverse_lazy('Listar-Noticia')


