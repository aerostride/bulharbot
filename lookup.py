#snippet used only to print available lyrics from genius to user console

#get API stuff

import lyricsgenius

#print list of songs from author

genius = lyricsgenius.Genius("REDACTED")
artist = genius.search_artist("CA$HANOVA BULHAR")
print(artist.songs)
