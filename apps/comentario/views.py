from django.shortcuts import render

from apps.comentario.models import Comentario
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ComentarioForm, CommentForm

# Create your views here.

"""
class CreateComment(CreateView):
    model = Comentario
    template_name = 'comentario/addComentario.html'
    #form_class = CommentForm
    fields = '__all__'
    success_url = reverse_lazy('home')
"""
def CreateComment(request):
	form = CommentForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addComentario3.html', context)

def AddComentario(request):
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addComentario.html', context)

def Comentarios(request):
	return render(request,'comentario/listarcomentario.html')

