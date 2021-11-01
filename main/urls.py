from django.contrib import admin
from django.urls import path, include
from .views import home, search

urlpatterns = [
    path('', home, name="home"),
    path('search/', search, name="search-url"),
]
