from django.http import HttpResponse
from users.forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#     form = LoginUserForm()
#     return render(request, 'users/login.html', {'form': form})

# def logout_user(request):
#     return HttpResponse('logout')
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:test')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        return context
    def form_valid(self, form):
        user = form.save() # сохранение пользователя
        login(self.request, user)
        return redirect('users:test')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:test')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        return context

    def get_success_url(self):
        return reverse_lazy('users:test')

def logout_user(request):
    logout(request)
    return redirect('users:login')

def test_func(request):
    return render(request, 'users/signup.html')