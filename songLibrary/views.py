from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
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