from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
#LO AGREGUE DE CHRISTIAN
from distutils.command.upload import upload
from email.policy import default

# Create your models here.

class Usuario(AbstractUser):
	imagen = models.ImageField(upload_to='usuario', default='usuario/user-default.png')
#	telefono = 
#	direccion =		
#		hay que agregar los demas atributos

	def get_absolute_url(self):
		return reverse('index')
		
