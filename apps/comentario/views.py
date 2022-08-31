from .models import Comentario
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView


class MostrarComentarios(ListView):
    model = Comentario
    template_name = 'noticia/noticia.html'
    ordering = ['-id']


class AddComentario(DetailView):
    model = Comentario
    template_name= "noticia/addComentario.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = Comentario.objects.all()
        return context

# class DeleteComentario(DeleteView):
#     model = Comentario
#     template_name = 'comentario/eliminarComentario.html'
#     success_url = reverse_lazy('Listar-Noticia')

def Comentarios(request):
    return render(request,'comentario/listarComentarios.html')


def ListarComentarios(request):
    comentarios = Comentario.objects.all()
    context = {
        "comentarios": comentarios,
    }
    return render(request, 'noticia/listarCategoria.html', context)