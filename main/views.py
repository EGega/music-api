from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    return HttpResponse('''<div class="container">
    <div class="artist">
      <h2>Artists</h2>
      <ul>
        <li><a href="/musicians/artists-list">Get Artists</a> </li>
        <li><a href="/musicians/artist-create">Add an Artist</a></li>
        <li><a href="/musicians/artist-delete/1">Delete an Artist</a></li>
        <li><a href="/musicians/artist-update/1">Update an Artist</a> </li>
      </ul>
    </div>
    <div class="album">
      <h2>Albums</h2>
      <ul>
        <li><a href="/musicians/albums-list">Get Albums</a> </li>
        <li><a href="/musicians/album-create">Add an Album</a></li>
        <li><a href="/musicians/album-delete/1">Delete an Album</a></li>
        <li><a href="/musicians/album-update/1">Update an Album</a> </li>
      </ul>
    </div>
    <div class="lyrics">
      <h2>Lyrics</h2>
      <ul>
        <li><a href="/musicians/lyrics-list">Get Lyrics</a> </li>
        <li><a href="/musicians/lyric-create">Add Lyrics</a></li>
        <li><a href="/musicians/lyric-delete/1">Delete Lyrics</a></li>
        <li><a href="/musicians/lyric-update/1">Update Lyrics</a> </li>
      </ul>
    </div>
    <div class="songs">
      <h2>Songs</h2>
      <ul>
        <li><a href="/musicians/songs-list">Get Songs</a> </li>
        <li><a href="/musicians/song-create">Add an Song</a></li>
        <li><a href="/musicians/song-delete/1">Delete an Song</a></li>
        <li><a href="/musicians/song-update/1">Update an Song</a> </li>
      </ul>
    </div>
    
  </div>''')

# def home_page(request):
#     return render(request, "../templates/index.html")