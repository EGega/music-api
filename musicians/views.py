from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Artist, Album, Lyric, Song

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistSerializer, AlbumSerializer, LyricSerializer, SongSerializer


@api_view()  # default GET
def home(request):
    return Response({'home': 'This is musicians page...'})


#Artist

@api_view(['GET'])
def artists_list(request):
    artists = Artist.objects.all()
    # print(students)
    serializer = ArtistSerializer(artists, many=True)
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def artist_create(request):
   serializer = ArtistSerializer(data=request.data)
   if serializer.is_valid():
    serializer.save()
    message = {
        "message:" f'Artist Created Successfully'
    }
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   else:
     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def artist_update(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    serializer = ArtistSerializer(instance=artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Artist updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def artist_delete(request, pk):
    student = get_object_or_404(Artist, id=pk)
    student.delete()
    message = {
        "message": 'Student deleted succesfully....'
    }
    return Response(message)



#Album
@api_view(['GET'])
def albums_list(request):
    albums = Album.objects.all()
    # print(students)
    serializer = AlbumSerializer(albums, many=True)
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def album_create(request):
   serializer = AlbumSerializer(data = request.data)
   if serializer.is_valid():
    serializer.save()
    message = {
        "message:" f'Album Created Successfully'
    }
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def album_update(request, pk):
    album = get_object_or_404(Album, id=pk)
    serializer = AlbumSerializer(instance=album, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Album updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def album_delete(request, pk):
    student = get_object_or_404(Album, id=pk)
    student.delete()
    message = {
        "message": 'Student deleted succesfully....'
    }
    return Response(message)




# Lyric

@api_view(['GET'])
def lyrics_list(request):
    lyrics = Lyric.objects.all()
    # print(students)
    serializer = LyricSerializer(lyrics, many=True)
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def lyric_create(request):
   serializer = LyricSerializer(data = request.data)
   if serializer.is_valid():
    serializer.save()
    message = {
        "message:" f'Lyrics Created Successfully'
    }
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def lyric_update(request, pk):
    lyric = get_object_or_404(lyric, id=pk)
    serializer = LyricSerializer(instance=Lyric, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Lyric updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def lyric_delete(request, pk):
    student = get_object_or_404(Lyric, id=pk)
    student.delete()
    message = {
        "message": 'Student deleted succesfully....'
    }
    return Response(message)
# Song

@api_view(['GET'])
def songs_list(request):
    songs = Song.objects.all()
    # print(students)
    serializer = SongSerializer(songs, many=True)
    # print(serializer)
    # print(serializer.data)
    return Response(serializer.data)

@api_view(["POST"])
def song_create(request):
   serializer = SongSerializer(data=request.data)
   if serializer.is_valid():
    serializer.save()
    message = {
        "message:" f'Song Created Successfully'
    }
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def song_update(request, pk):
    song = get_object_or_404(song, id=pk)
    serializer = SongSerializer(instance=Song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Song updated succesfully....'
        }
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def song_delete(request, pk):
    student = get_object_or_404(Song, id=pk)
    student.delete()
    message = {
        "message": 'Student deleted succesfully....'
    }
    return Response(message)