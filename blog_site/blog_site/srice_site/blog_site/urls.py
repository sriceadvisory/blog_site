from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.posts_detail, name="posts_detail")
]