from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm  

class Login(LoginView):
    
    form_class = LoginForm
    template_name = 'original/login.html'