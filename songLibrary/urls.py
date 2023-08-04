from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = 'index'),
    path('song-list/', views.songList, name = 'song-list'),
    path('artist-detail/<str:pk>/', views.artistDetail, name='artist-detail'),
    path('get-users/', views.getUsers, name = 'get-users'),
    path('create-user/', views.createUser, name = 'create-user'),
    path('update-user/<str:pk>/', views.updateUser, name = 'update-user'),
    path('delete-user/<str:pk>/', views.deleteUser, name = 'delete-user'),
]
