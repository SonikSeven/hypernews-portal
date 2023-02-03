from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    re_path("^news/?$", views.MainView.as_view(), name="main_url"),
    path("", RedirectView.as_view(pattern_name="main_url")),
    re_path(r"^news/(?P<article_number>\d+)/?$", views.ArticleView.as_view()),
    re_path("^news/create/?$", views.AddArticleView.as_view(), name="add_article_url"),
]
