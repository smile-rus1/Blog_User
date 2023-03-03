from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator

from .views import *
from .models import *


class RegisterUserForm(UserCreationForm):
    validator_pass = RegexValidator(r'^[0-9a-zA-Z]*$', "Пароль должен состоять только из цифр и букв!")

    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password1 = forms.CharField(label="Введите пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}),
                                validators=[validator_pass], min_length=8, max_length=24)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={"class": "form-input"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Введите пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}))
