from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('guitars-with-songs', views.guitars_with_songs)
]
