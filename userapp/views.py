from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import RegisterForm


class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    next_page = 'store:index'

   
class LoginUserView(LoginView):
    template_name='login.html'
    next_page = 'store:index'


class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page='store:index'