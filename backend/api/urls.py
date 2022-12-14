from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('guitars-with-songs/', views.guitars_with_songs),
    path('media/', views.youtube_spotify_pairs),
    path('3d-models/', views.guitar_ids_with_3d_models)
]
