from django.urls import path
from . import views

urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view()),
    path('addCategoria/', views.AddCategoria.as_view()),
    path('updateNoticia/<int:pk>', views.UpdateNoticia.as_view(), name='Update-Notice'),
    path('eliminarNoticia/<int:pk>', views.DeleteNoticia.as_view(), name='Eliminar-Noticia'),
    path('detail/<int:pk>', views.DetailNoticia.as_view(), name='Detail-Noticia'),
    path('listarNoticia/', views.ListarNoticia, name='Listar-Noticia'),
    path('listarCategoria/<str:categoria>', views.ListarNoticiaPorCategoria),
    ################# Comentario repo Gaston ####################
    path('notice/<int:pk>/addComment/', views.CreateComentario.as_view(), name='add_comment'),

]
