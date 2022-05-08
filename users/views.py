from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import UserCreationForm
from .models import User


class Login(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    next_page = 'home'


class Logout(LogoutView):
    next_page = 'login'


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return super().form_valid(form)


