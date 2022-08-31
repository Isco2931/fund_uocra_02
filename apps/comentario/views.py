from ast import Delete
from .models import Comentario
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView

class MostrarComentarios(ListView):
    model = Comentario
    template_name = 'noticia/noticia.html'
    ordering = ['-id']

class AddComentario(DetailView):
    model = Comentario
    template_name= "comentario/addComment.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = Comentario.objects.all()
        return context

def Comentarios(request):
    return render(request,'comentario/listarComentarios.html')
