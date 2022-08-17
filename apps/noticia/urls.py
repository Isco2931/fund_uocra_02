from django.urls import path
from . import views

urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view()),
    path('addCategoria/', views.AddCategoria.as_view()),
#    path('listanoticia/', views.ListaNoticia.as_views()),
    path('listarNoticia/', views.ListarNoticia),
    path('listarCategoria/<str:categoria>', views.ListarNoticiaPorCategoria),
]