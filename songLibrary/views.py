from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer, ArtistSerializer, UserSerializer

from .models import Song, Artist
# This view below makes it so when the user loads the front page of the API, it shows them all the possible URL paths
# Makes the API more user friendly
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'songlist' : '/song-list/', # Displays all the songs in the database
        'artistdetail' : '/artist-list/<str:pk>', # Displays artist and their songs 
        'createUser' : '/create-user/', # Create a user
        'deleteUser' : '/delete-user/<str:pk>'
    }

    return Response(api_urls)


# This function takes all of the songs in the Song model and stores them in a variable, songs
# Then it serializes the data using the SongSerializer created in the Serializers.py file and stores that in a variable, serializer
# When the user goes to the URL /song-list/ it will return all of the serialized data
# For this instance it will return an ID and the song title based on how the model is defined

@api_view(['GET'])
def songList(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artistDetail(request, pk):
    artists = Artist.objects.get(id=pk)
    serializer = ArtistSerializer(artists, many=False)
    return Response(serializer.data)

#REST framework introduces a Request object that extends the regular HttpRequest
# Core functionality is the request.data attribute, which is similar to request.POST

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


