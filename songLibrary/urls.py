from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = 'index'),
    path('song-list/', views.songList, name = 'song-list'),
]
