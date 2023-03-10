from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="home"),
    path("register/", register, name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("add_new_post/", add_new_post, name="add_new_post"),
    path("post/<int:post_id>/", show_post, name="post"),
    path("my_post/", my_posts, name="my_post"),

]
