from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст статьи")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", auto_created=True)
    date_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Посты пользователей"
        ordering = ["-date_update"]

