from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context_processors import request
from django.urls import reverse_lazy

from .forms import *


def index(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
    }
    return render(request, "index.html", context=context)


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


def add_new_post(request):
    if request.method == "POST":
        form = AddNewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            Post.objects.create(title=title, content=content, user_id=request.user.id)

            return redirect("home")
    else:
        form = AddNewPostForm()

    context = {
        "title": "Новый пост",
        "form": form,
    }

    return render(request, "add_new_post.html", context=context)


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
    messages.success(request, f"Вы вышли с аккаунта")
    return redirect("home")


@login_required
def profile(request):
    return render(request, 'profile.html')
