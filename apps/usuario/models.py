from django.db import models
from django.contrib.auth.models import AbstractUser
#LO AGREGUE DE CHRISTIAN
from distutils.command.upload import upload
from email.policy import default
from turtle import mode

# Create your models here.

class Usuario(AbstractUser):
	imagen = models.ImageField(upload_to='usuario', default='usuario/user-default.png')
#	telefono = 
#	direccion =		
#		hay que agregar los demas atributos
		
