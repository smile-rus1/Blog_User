from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    # slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name="Текст статьи")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", auto_created=True)
    date_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name_plural = "Посты пользователей"
        ordering = ["-date_update"]

