from django.shortcuts import render
from django.http import JsonResponse

# Decorators restrict access to views based on the request method (GET, POST, DELETE etc.)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer, ArtistSerializer, UserSerializer

from .models import Song, Artist, User
# This view below makes it so when the user loads the front page of the API, it shows them all the possible URL paths
# Makes the API more user friendly
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'songlist' : '/song-list/', # Displays all the songs in the database
        'artistdetail' : '/artist-list/<str:pk>', # Displays artist and their songs 
        'getUsers' : '/get-users/', # Displays all the users in the database
        'createUser' : '/create-user/', # Create a user
        'updateUser' : '/update-user/<str:pk>', # Update user info
        'deleteUser' : '/delete-user/<str:pk>',
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

# This function takes all the artists and returns all of their song titles
@api_view(['GET'])
def artistDetail(request, pk):
    artists = Artist.objects.get(id=pk)
    serializer = ArtistSerializer(artists, many=False)
    return Response(serializer.data)

# REST framework introduces a Request object that extends the regular HttpRequest
# Core functionality is the request.data attribute, which is similar to request.POST

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST']) ## CREATE
def createUser(request):
    serializer = UserSerializer(data=request.data) #Creating an instance of UserSerializer, data being initialized with the data from the HTTP request method
    
    if serializer.is_valid(): # This makes sure required fields are all there
        serializer.save() # Once all the fields are retrieved, save it to the database

    return Response(serializer.data) 

@api_view(['POST']) ## UPDATE
def updateUser(request, pk):
    user = User.objects.get(id=pk) #Get the user id by the pk passed in as an argument
    serializer = UserSerializer(instance=user, many=False)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk) # Get the user id and delete it from the database
    user.delete()

    return Response('User successfully deleted!')

