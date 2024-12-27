from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist, related_name='songs')
    duration = models.DurationField()
    
    def __str__(self):
        artists = ", ".join(artist.name for artist in self.artist.all())
        return f'{self.title} by {artists}'


class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    artists = models.ManyToManyField(Artist, related_name='albums')
    songs = models.ManyToManyField(Song, related_name='albums')