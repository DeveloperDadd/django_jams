from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = 'index'),
    path('song-list/', views.songList, name = 'song-list'),
    path('artist-detail/<str:pk>/', views.artistDetail, name='artist-detail'),
    path('create-user/', views.createUser, name = 'create-user'),
]
