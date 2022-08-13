from django.shortcuts import render #, redirect
from django.views import View
#from django.contrib.auth.views import LoginView, LogoutView
#from .forms import userForm, loginForm
#from django.contrib.auth.views import LoginView

def Index(request):
    return render(request, 'index.html')
#HASTA ACÁ ESTA MI PROYECTO, LO SIGUIENTE ES LO DE ABI 

def basic(request):
    return render(request, 'pages/basic-grid.html')

def full(request):
    return render(request, 'pages/full-width.html')

def galeria(request):
    return render(request, 'pages/gallery.html')

def sidebar_left(request):
    return render(request, 'pages/sidebar-left.html')

def sidebar_right(request):
    return render(request, 'pages/sidebar-right.html')
