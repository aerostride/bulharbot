import lyricsgenius
import random
import tweepy

keys = {
    'CONSUMER_API_KEY': 'PxQm7SnUgcJP97JiRjG5YJtqw',
    'CONSUMER_API_SECRET_KEY': 'rrdbt2sZu0rM0Bfx3tKdvgJjDloflnfZihgidC1OFJomOMqKRA',
    'ACCESS_TOKEN': '1194034435693395968-rkp1b2tF24lMCqsGD6vdsWcCPsMfoB',
    'ACCESS_TOKEN_SECRET': 'E6Y9NxfB1XlvwpVafRgjgcbaS40tJ1H0iTbgIy3UeBMlL'
}

all_songs = ["Off Season", "Swag Martin Fenin", "MVP", "Šárka Peková", "Neni to moje vina", "Kariéra neni", "Tom Brady Freestyle", "Party u mě doma", "Primitivo", "Dej mi cash", "Zkurveně sám", "Nejkrásnější portrét", "B.M.W.", "Sem sober", "Champions League", "Free Nikolai Ivanov", "Airport směr Milano", "Kellner", "Bollywood", "Napalm", "Bollywood (Dopelphin Remix)", "Ballar jako Fotr", "Cejtim se jak Pacanda", "Sick Day"]

def get_raw_lyrics():
    genius_client_access_token = "dJNe8EO8x0pz-MvoLtTL5W1xKcqBFxP5MBErlJCujK0ViilzCAEbFfaeNlVLz_eu"
    genius = lyricsgenius.Genius(genius_client_access_token)
    random_song_title = random.choice(all_songs)
    lyrics = genius.search_song(random_song_title, "CA$HANOVA BULHAR").lyrics
    song = random_song_title.upper()
    songlower = random_song_title
    return lyrics, songlower, song

def get_tweet_from(lyrics, songlower):
    lines = lyrics.split('\n')
    for index in range(len(lines)):
        if lines[index] == "" or "[" in lines[index]:
            lines[index] = "XXX"
    lines = [i for i in lines if i != "XXX"]
    random_num = random.randrange(0, len(lines)-1)
    tweet = lines[random_num] + "\n" + lines[random_num+1] + "\n" + "\n" + "CA$HANOVA BULHAR" + " " + "-" + " " + songlower
    tweet = tweet.replace("\\", "")
    return tweet

def handler(event, context):
    auth = tweepy.OAuthHandler(
        keys['CONSUMER_API_KEY'],
        keys['CONSUMER_API_SECRET_KEY']
    )
    auth.set_access_token(
        keys['ACCESS_TOKEN'],
        keys['ACCESS_TOKEN_SECRET']
    )
    api = tweepy.API(auth)
    lyrics, songlower, song = get_raw_lyrics()
    tweet = get_tweet_from(lyrics, songlower)
    status = api.update_status(tweet)
    bio = api.update_profile(description=song)

    return tweet
