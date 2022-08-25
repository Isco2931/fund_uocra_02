from django.shortcuts import render #, redirect
from django.views import View
from django.urls import reverse
#from django.contrib.auth.views import LoginView, LogoutView
#from .forms import userForm, loginForm
#from django.contrib.auth.views import LoginView

def Index(request):
    return render(request, 'index.html')

def About(request):
    return (render(request, 'about.html'))

def Contact(request):
    return render(request, 'contact.html')


