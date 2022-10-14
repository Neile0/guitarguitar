from urllib import request
import requests

guitarsWithSongsUrl = 'http://services.guitarguitar.co.uk/WebService/api/hackathon/guitarswithsongs'
guitarsUrl = 'https://services.guitarguitar.co.uk/WebService/api/hackathon/guitars'

def get_guitars_with_songs(*args, **kwargs):
    data = requests.get(guitarsWithSongsUrl)
    return data.json()


def get_guitars(*args, **kwargs):
    data = requests.get(guitarsUrl)
    return data.json()