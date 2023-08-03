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
