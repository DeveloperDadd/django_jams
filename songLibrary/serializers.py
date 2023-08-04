from rest_framework import serializers
from .models import Song, Artist, User

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'songs')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'