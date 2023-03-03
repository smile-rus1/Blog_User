from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import *


def index(request):
    title = {"title": "home"}
    return render(request, "index.html", context=title)


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Создан аккаунт {username}")

            return redirect("login")
        else:
            pass
    else:
        form = RegisterUserForm()

    context = {
        "title": "Регистрация",
        "form": form,
    }

    return render(request, "register.html", context=context)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        change = {"title": "Авторизация"}
        return context | change

    def get_success_url(self):
        return reverse_lazy("home")


def logout_user(request):
    logout(request)
    return redirect("home")


@login_required
def profile(request):
    return render(request, 'profile.html')
