from django.urls import path
from . import views

urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view()),
    path('addCategoria/', views.AddCategoria.as_view()),
#    path('listarCategoria/', views.ListarCategoria.as_view()),
    path('listarNoticia/', views.ListarNoticia),
    path('listarCategoria/<str:categoria>', views.ListarNoticiaPorCategoria),
]