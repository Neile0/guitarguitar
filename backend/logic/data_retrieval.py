from urllib import request
import requests

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
        youtube = obj['youtube']
        youtubeEmbed = youtube.replace("https://youtube.com/", "https://www.youtube.com/embed/")
        pair['youtube'] = youtubeEmbed
        pair['spotify'] = "https://open.spotify.com/embed/track/" + obj['spotifyId']
        pairs.append(pair)
    return pairs