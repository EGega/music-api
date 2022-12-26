from django.contrib import admin

# Register your models here.
from .models import Artist, Album, Lyric, Song

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Lyric)
admin.site.register(Song)