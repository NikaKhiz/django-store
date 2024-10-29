from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



class LoginUserView(LoginView):
    template_name='login.html'


class RegisterUserView(View):
    
    def get(self, request):
        
        return render(request, 'register.html')

    def post(self, request):
        ...


class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page='store:index'