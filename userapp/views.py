from django.shortcuts import render
from django.contrib.auth.views import LoginView


class LoginUserView(LoginView):
    template_name='login.html'
    next_page = 'store:index'
