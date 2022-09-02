from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Noticia, Categoria
from apps.comentario.models import Comentario
from django.views.generic import View
from apps.comentario.forms import ComentarioForm
from django.shortcuts import render, redirect


############# NOTICIAS ##############################################


class AddNoticia(CreateView):
    model = Noticia
    fields = ['usuario', 'titulo', 'texto', 'categoria', 'imagen']
    template_name = 'noticia/addNoticia.html'
    success_url = reverse_lazy('Listar-Noticia')


class UpdateNoticia(UpdateView):
    model = Noticia
    fields = ['usuario', 'titulo', 'texto', 'categoria', 'imagen']
    template_name = 'noticia/updateNoticia.html'
    success_url = reverse_lazy('Listar-Noticia')


class DeleteNoticia(DeleteView):
    model = Noticia
    template_name = 'noticia/eliminarNoticia.html'
    success_url = reverse_lazy('Listar-Noticia')


class DetailNoticia(DetailView):
    model = Noticia
    template_name = 'noticia/detailNoticia.html'


class ListarNoticia(View):
    def get(self, request, pk, *args, **kwargs):
        noticia = Noticia.objects.get(pk=pk)
        form = ComentarioForm()
        comentarios = Comentario.objects.filter(noticia=pk).order_by('fecha') # agregar - para ordenar de forma descendente
        context = {
              'noticia': noticia,
          'form': form,
          'comentarios': comentarios,
          }
        return render(request, 'noticia/noticia.html', context)

    def post(self, request, pk, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            noticia = Noticia.objects.get(pk=pk)
            form.instance.usuario = request.user
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


def ListarNoticia2 (request):
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
    return context


################# Comentarios ################################################


class CreateComentario(CreateView):
    model = Comentario
    template_name = 'comentario/addComentario2.html'
    fields = ['usuario','noticia','comentario', ]
    success_url = reverse_lazy('Listar-Noticia')

class DeleteComentario(DeleteView):
    model = Comentario
    template_name = 'comentario/eliminarComentario.html'
    success_url = reverse_lazy('Listar-Noticia')



########### CATEGORIAS ################################################


class AddCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'noticia/addCategoria.html'
    success_url = reverse_lazy('categoria')


class DeleteCategoria(DeleteView):
    model = Categoria
    template_name = 'noticia/eliminarCategoria.html'
    success_url = reverse_lazy('categoria')





