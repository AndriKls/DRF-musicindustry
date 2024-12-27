from rest_framework import viewsets
from .models import Artist, Song, Album
from .serializers import AlbumDetailSerializer, ArtistListSerializer, ArtistDetailSerializer, ArtistCreateSerializer, SongListSerializer, SongDetailSerializer, AlbumListSerializer, AlbumCreateSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.


class ArtistViewSet(viewsets.ViewSet):
    
    def list(self, request):
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Artist.objects.all()
        artists = get_object_or_404(queryset, pk=pk)
        serializer = ArtistDetailSerializer(artists)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArtistCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk):
        platform = Artist.objects.get(pk=pk)
        platform.delete()
        return Response(status=204)

class SongViewSet(viewsets.ViewSet):
    def list(self, request):
        songs = Song.objects.all()
        serializer = SongListSerializer(songs, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Song.objects.all()
        song = get_object_or_404(queryset, pk=pk)
        serializer = SongDetailSerializer(song)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = SongDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(status=204)


class AlbumViewSet(viewsets.ViewSet):
    
    def list(self, request):
        albums = Album.objects.all()
        serializer = AlbumListSerializer(albums, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Album.objects.prefetch_related('artists', 'songs')
        album = get_object_or_404(queryset, pk=pk)
        serializer = AlbumDetailSerializer(album)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = AlbumCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
        
    
    def destroy(self, request, pk):
        album = Album.objects.get(pk=pk)
        album.delete()
        return Response(status=204)