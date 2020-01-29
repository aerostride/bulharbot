#snippet used only to print available lyrics from genius to user console

import lyricsgenius

genius = lyricsgenius.Genius("REDACTED")
artist = genius.search_artist("CA$HANOVA BULHAR")
print(artist.songs)
