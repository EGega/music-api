from rest_framework import serializers
from .models import Artist, Album, Lyric, Song

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ["id","first_name", "last_name", "artist_pic", "num_stars"]

class AlbumSerializer(serializers.ModelSerializer):
  artist = ArtistSerializer(many = True)
  class Meta:
    model = Album
    fields = ["artist", "name", "released", "cover"]

class LyricSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lyric
    fields = ["title", "content"]


class SongSerializer(serializers.ModelSerializer):
  # artist = ArtistSerializer(many = True)
  # album = AlbumSerializer(many = True) #available for only many to many fields
  class Meta:
    model = Song
    fields = ["artist", "album", "released", "lyric", "name"]