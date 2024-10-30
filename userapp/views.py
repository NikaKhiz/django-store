from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginUserView(LoginView):
    template_name='login.html'
    next_page = 'store:index'


class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page='store:index'