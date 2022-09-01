from django.urls import path
from . import views

urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view()),
    path('addCategoria/', views.AddCategoria.as_view(), name='categoria'),
    path('updateNoticia/<int:pk>', views.UpdateNoticia.as_view(), name='Update-Notice'),
    path('eliminarNoticia/<int:pk>', views.DeleteNoticia.as_view(), name='Eliminar-Noticia'),
    path('noticia/<int:pk>', views.DetailNoticia.as_view(), name='Detail-Noticia1'),
    path('listarNoticia/', views.ListarNoticia2, name='Listar-Noticia'),
    path('listarCategoria/<str:categoria>', views.ListarNoticiaPorCategoria),
    path('listarCategoria/', views.ListarCategoria, name='ListCategoria'),
    path('notice/<int:pk>/addComment/', views.CreateComentario.as_view(), name='add_comment'),
    path('detail/<int:pk>', views.ListarNoticia.as_view(), name='Detail-Noticia'),
    path('eliminarCategoria/<int:pk>', views.DeleteCategoria.as_view(), name='Eliminar-Categoria'),
]
