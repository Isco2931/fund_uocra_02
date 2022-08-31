from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Noticia, Categoria
from apps.comentario.models import Comentario
from django.views.generic import View
from apps.comentario.forms import CommentForm

class AddNoticia(CreateView):
    model = Noticia
    fields = ['autor', 'titulo', 'texto', 'categoria', 'imagen']
    template_name = 'noticia/addNoticia.html'
    success_url = reverse_lazy('index')
class AddCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'noticia/addCategoria.html'
    success_url = reverse_lazy('index')

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
class UpdateNoticia(UpdateView):
    model = Noticia
    fields = ['autor', 'titulo', 'texto', 'categoria', 'imagen']
    template_name = 'noticia/updateNoticia.html'
    success_url = reverse_lazy('Listar-Noticia')
class DeleteNoticia(DeleteView):
    model = Noticia
    template_name = 'noticia/eliminarNoticia.html'
    success_url = reverse_lazy('Listar-Noticia')

################# Contextos ####################

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

################# Comentario Christian ####################
class ListarNoticia1(View):
    def get(self, request, pk, *args, **kwargs):
        noticia = Noticia.objects.get(pk=pk)
        form = CommentForm()
        comentarios = Comentario.objects.filter(noticia=pk).order_by('-fecha') # agregar - para ordenar de forma descendente
        context = {
            'noticia': noticia,
            'form': form,
            'comentarios': comentarios,
            }
        return render(request, 'noticia/noticia.html', context)

    def post(self, request, pk, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            noticia = Noticia.objects.get(pk=pk)
            form.instance.autor = request.user
            form.instance.noticia = noticia
            form.save()
            return redirect('Detail-Noticia', pk=pk)

        comentarios = Comentario.objects.filter(noticia=pk).order_by('-fecha')

        context = {
            'noticia': noticia,
            'form': form,
            'comentarios': comentarios
        }
        return render(request, 'noticia/noticia.html', context)