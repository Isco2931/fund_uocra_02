from django.urls import path
from . import views

urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view(), name='addCategoria'),
    path('addCategoria/', views.AddCategoria.as_view()),
    path('updateNoticia/<int:pk>', views.UpdateNoticia.as_view(), name='Update-Notice'),
    path('eliminarNoticia/<int:pk>', views.DeleteNoticia.as_view(), name='Eliminar-Noticia'),
    path('listarNoticia/', views.ListarNoticia, name='Listar-Noticia'),
    path('listarCategoria/<str:categoria>', views.ListarNoticiaPorCategoria),
    path('detail/<int:pk>', views.ListarNoticia1.as_view(), name='Detail-Noticia'),
    path('eliminarCategoria/<int:pk>', views.DeleteCategoria.as_view(), name='Eliminar-Categoria'),
]

