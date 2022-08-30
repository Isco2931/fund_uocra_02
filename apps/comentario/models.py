from django.db import models
from apps.noticia.models import Noticia
from apps.usuario.models import Usuario

# Create your models here.

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=250, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
