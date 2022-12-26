from django.urls import path
from .views import (home,
artists_list,
albums_list,
lyrics_list,
songs_list,
artist_create,
album_create,
lyric_create,
song_create,
artist_update,
artist_delete,
album_update,
album_delete,
lyric_update,
lyric_delete,
song_update,
song_delete
)

urlpatterns = [
  path("", home),
  #artist path
  path("artists-list", artists_list, name="list"),
  path("artist-create", artist_create, name="create"),
  path("artist-update/<int:pk>/", artist_update, name="update"),
  path("artist-delete/<int:pk>/", artist_delete, name="delete"),
 #album path
  path("albums-list", albums_list, name="list"),
  path("album-create", album_create, name="create"),
  path("album-update/<int:pk>/", album_update, name="update"),
  path("album-delete/<int:pk>/", album_delete, name="delete"),
 #lyrics path
  path("lyrics-list", lyrics_list, name="list"),
  path("lyric-create", lyric_create, name="create"),
  path("lyric-update/<int:pk>/", lyric_update, name="update"),
  path("lyric-delete/<int:pk>/", lyric_delete, name="delete"),
 #song path
  path("songs-list", songs_list, name="list"),
  path("song-create", song_create, name="create"),
  path("song-update/<int:pk>/", song_update, name="update"),
  path("song-delete/<int:pk>/", song_delete, name="delete"),
]


