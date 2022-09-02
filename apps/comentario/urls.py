from django.urls import path
from . import views

urlpatterns = [
        path('eliminarComentario/<int:pk>', views.DeleteComentario.as_view(), name='Eliminar-Comentario')
]