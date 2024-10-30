from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm


class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('store:index')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.is_staff = True
        form.save()
        return super().form_valid(form)

   
class LoginUserView(LoginView):
    template_name='login.html'
    next_page = 'store:index'


class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page='store:index'