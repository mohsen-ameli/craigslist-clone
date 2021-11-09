from django.contrib import admin
from django.urls import path, include
from .views import home, search

app_name = "main"
urlpatterns = [
    path("", home, name="home"),
    path("search/", search, name="search-url"),
]
