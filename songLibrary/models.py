from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Song_Genre(models.Model):
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete= models.CASCADE)
    
class User(models.Model):
    username = models.CharField(max_length=16)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Artist(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name
    
class Song_Artist(models.Model):
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    artist_id = models.ForeignKey(Artist, on_delete= models.CASCADE)

class Album(models.Model):
    name = models.CharField(max_length=200)

class Artist_Album(models.Model):
    artist_id = models.ForeignKey(Artist, on_delete = models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete= models.CASCADE)

class Album_Songs(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    #### order ####

class User_Playlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class User_Playlist_Songs(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    user_playlist_id = models.ForeignKey(User_Playlist, on_delete=models.CASCADE)