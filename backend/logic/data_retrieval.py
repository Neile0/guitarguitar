from urllib import request
import requests
import os

guitarIdLookupField = 'skU_ID'

guitarsWithSongsUrl = 'http://services.guitarguitar.co.uk/WebService/api/hackathon/guitarswithsongs'
guitarsUrl = 'https://services.guitarguitar.co.uk/WebService/api/hackathon/guitars'

def get_guitars_with_songs():
    data = requests.get(guitarsWithSongsUrl)
    return data.json()

def get_guitars():
    data = requests.get(guitarsUrl)
    return data.json()

def get_guitar(id):
    guitars = get_guitars()
    for guitar in guitars:
        if guitar[guitarIdLookupField] == id:
            return guitar

def get_youtube_spotify_pairs():
    data = get_guitars_with_songs()
    pairs = []
    for obj in data:
        pair = {}
        youtube = obj['youtubeUrl']
        youtubeEmbed = youtube.replace("https://www.youtube.com/watch?v=", "https://www.youtube.com/embed/")
        pair['youtube'] = youtubeEmbed
        pair['spotify'] = "https://open.spotify.com/embed/track/" + obj['spotifyId'] + "?autoplay=1&controls=0&mute=0"
        pairs.append(pair)
    return pairs

def get_guitar_ids_with_models():
    dirs = [x[1] for x in os.walk('../guitarguitar/public/models')]
    return dirs[0]