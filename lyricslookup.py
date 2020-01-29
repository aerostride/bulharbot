import lyricsgenius

genius = lyricsgenius.Genius("your_client_access_token_here")
artist = genius.search_artist("your_artist")
print(artist.songs)
