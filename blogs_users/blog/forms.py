from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
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


class AddNewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

        widgets = {
            "title": forms.TextInput(),
            "content": forms.Textarea(attrs={"cols": 60, "rows": 10}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 30:
            raise ValidationError("Название поста не может быть больше 30 слов")

        return title

    def clean_content(self):
        content = self.cleaned_data["content"]
        if len(content) > 500:
            raise ValidationError("Вы привысили количество слов (MAX 500)")

        return content


class ChangePostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-input"}))

    class Meta:
        model = Post
        fields = ("title", "content")


