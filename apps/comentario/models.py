from django.db import models
from apps.noticia.models import Noticia
from apps.usuario.models import Usuario
from fund_uocra_02 import settings

# Create your models here.

class Comentario(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentario')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=250, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
#    imagen = models.ImageField(upload_to='comentario', null=True)

"""
class Comment(models.Model):
    post =  models.ForeignKey(Noticia, related_name="comentario", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    cuerpo = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    #def __str__(self):
    #    return '%s - %s' % (self.notice.titulo, self.name)
"""