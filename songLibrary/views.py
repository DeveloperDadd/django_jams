from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer

from .models import Song
# This view below makes it so when the user loads the front page of the API, it shows them all the possible URL paths
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'songlist' : '/song-list/',
        'songartist' : '/song-artist/<str:pk>',
        'songalbum' : '/song-album/<str:pk>',
        'userCreate' : '/create-user/',
        'deleteUser' : '/delete-user/<str:pk>'
    }

    return Response(api_urls)

@api_view(['GET'])
def songList(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)