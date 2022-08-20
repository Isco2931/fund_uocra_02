from django.urls import path
from . import views

urlpatterns = [
    path('addNoticia/', views.AddNoticia.as_view()),
    path('addCategoria/', views.AddCategoria.as_view()),
    path('updateNoticia/<int:pk>', views.UpdateNoticia.as_view(), name='Update-Notice'),
    path('eliminarNoticia/<int:pk>', views.DeleteNoticia.as_view(), name='Eliminar-Noticia'),
    path('detail/<int:pk>', views.DetailNoticia.as_view(), name='Detail-Noticia'),
#    path('listarCategoria/', views.ListarCategoria()),
    path('listarNoticia/', views.ListarNoticia, name='Listar-Noticia'),
    path('listarCategoria/<str:categoria>', views.ListarNoticiaPorCategoria)
    ,
]

"""
urlpatterns = [
    path('', views.HomeNotice.as_view(), name="home"),
    path('detail/<int:pk>', views.DetailNotice.as_view(), name='detail_notice'),
    path('addNoticia/', views.CreateNotice.as_view(), name='add_notice'),
    path('updateNotice/<int:pk>', views.UpdateNotice.as_view(), name='Update_Notice'),
    path('deleteNotice/<int:pk>', views.DeleteNotice.as_view(), name='Delete_Notice'),
]"""