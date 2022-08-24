from django.urls import path
from . import views

urlpatterns = [
    path('addComentario/', views.AddComentario, name="addComentario"),
    path('addComentario3/', views.CreateComment, name="addComentario3"),
]