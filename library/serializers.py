from rest_framework import serializers
from .models import Artist, Song, Album


class ArtistSerializerForAlbum(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name']

class AlbumListSerializer(serializers.ModelSerializer):
    artists = ArtistSerializerForAlbum(many=True)  # Include related artist names
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date', 'artists']

class AlbumSerializerForSongAndArtist(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title']

# Serializer for listing artist names only
class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'genre']  # Include only basic fields

# Serializer for retrieving a single artist with their songs
class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration']

class SongDetailSerializer(serializers.ModelSerializer):
    albums = AlbumSerializerForSongAndArtist(many=True, read_only=True)  # Include related albums
    artist = ArtistListSerializer(many=True)  # Include related artists
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'artist', 'albums']

class ArtistDetailSerializer(serializers.ModelSerializer):
    albums = AlbumSerializerForSongAndArtist(many=True)  # Include related albums
    songs = SongListSerializer(many=True)  # Include related songs
    

    class Meta:
        model = Artist
        fields = ['id', 'name', 'genre', 'albums', 'songs']  # Include all artist details and songs


class ArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'genre']


class AlbumDetailSerializer(serializers.ModelSerializer):
    artists = ArtistListSerializer(many=True)  # Include related artist
    songs = SongListSerializer(many=True)  # Include related songs
    
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date', 'artists', 'songs']

class AlbumCreateSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), many=True, required=False
    )
    songs = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(), many=True, required=False
    )


    class Meta:
        model = Album
        fields = ['title', 'release_date', 'artists', 'songs']
        extra_kwargs = {
            'id': {'read_only': True}
        }