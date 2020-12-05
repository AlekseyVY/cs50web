from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.get_search, name="search"),
    path("newPage", views.new_page, name="newPage"),
    path("<str:title>", views.page, name="page")
]
