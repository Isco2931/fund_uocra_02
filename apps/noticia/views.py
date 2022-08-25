from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
#LEER SOBRE VISTAS BASADAS EN CLASES Y VISTAS GENERICAS
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Noticia, Categoria
# Create your views here.

#    min 15:24
#
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
    categoria = Categoria.objects.all()
#   categoria_x_mes = Categoria.objects.flter()
    context = {
        'noticia': noticia,
        'categoria': categoria,
#        'categoriaxmes': categoria_x_mes,
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
    return render(request, 'category.html', context)
"""   
class ListarCategoria(ListView):
    model = Categoria
    template_name = 'base.html'

def ListarCategoria (request):
    categoria = Categoria.objects.all()
    context = {
        'categoria': categoria,
    }
    return render(request, 'base.html', context)
"""
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
"""
NO LA PUEDO USAR PORQUE LAS NOTICIAS TIENEN ESPACIOS Y EN LA URL NO RECONOCE LOS ESPACIOS POR ENDE NO MATCHEA CON LAS NOTICIAS
def DetailNoticia (request, noticia):
    noticia2 = Noticia.objects.filter(titulo=noticia)
    noticia1 = Noticia.objects.filter(noticia=noticia2[0].id)
    categoria = Categoria.objects.all()
    context = {
        'noticia': noticia1,
        'categoria': categoria,
    }
    return render(request, 'noticia/detailNoticia.html', context)
"""
from apps.comentario.models import Comentario
from apps.comentario.forms import ComentarioForm

################# Comentario repo Gaston ####################
class DetailNoticia2(DetailView):
    model = Noticia
    template_name = 'noticia/detailNoticia2.html'

    def ListarContexto (request):
        noticia = Noticia.objects.all()
        categoria = Categoria.objects.all()
        comentario = Comentario.objects.all()
        context = {
            'noticia': noticia,
            'categoria': categoria,
            'comentario': comentario,
        }
        return render(request, 'noticia/detailNoticia2.html', context)

class CreateComentario(CreateView):
    model = Comentario
    template_name = 'comentario/addComentario2.html'
    fields = ['comentario']
    exclude = ['autor', 'noticia']
    #form_class = CommentForm
    fields = '__all__'
    success_url = reverse_lazy('index')




################# Comentario repo Augusto ####################



from django.core.cache import cache
from django.contrib.auth import views as auth
from django.views import View

def ReadPost(request, id):
	try:
		posts = ExistePost(id)
	except Exception:
		posts = Noticia.objects.get(id=id)
	comentarios = Comentario.objects.filter(post=id)

	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		if request.user.is_authenticated:
			aux =  form.save(commit=False)
			aux.Noticia = posts
			aux.Usuario = request.Usuario
			aux.save()
			form = ComentarioForm()
		else:
			return redirect('usuario:login')
	
	context = {
		'titulo': 'post',
		'posts': posts,
		'form': form,
		'comentarios': comentarios
	}
	return render(request,'noticia/detailNoticia2.html', context)


def ExistePost(id):
	for i in cache.get('posts'):
		if i.id == id:
			return i
	return None

################# Contexto Categorias repo Chuki ####################

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

