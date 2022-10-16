from operator import indexOf
from logic.data_retrieval import get_guitars_with_songs, get_guitars, get_guitar

guitarIDLookupField = 'skU_ID'

aGuitarId = '12050912030058'
aSpotifyId = "7BsPyswBtiM1PbPnUnuNzE?si=93175f88875b4d3c"
aUrl = "https://www.youtube.com/watch?v=qjEqt_cpey8"

def get_guitar_from_spotify_id(id):
    data = get_guitars_with_songs()
    for guitar in data:
        if id == guitar['spotifyId']:
            return guitar[guitarIDLookupField]
    return False
    
def get_guitar_from_youtube(url):
    data = get_guitars_with_songs()
    for guitar in data: 
        if url == guitar['youtubeUrl']:
            return guitar[guitarIDLookupField]
    return False 

def get_guitars_with_matching(guitarID, lookupField):
    guitars = get_guitars()
    print(guitars)
    searchingGuitar = get_guitar(guitarID)
    criteria = searchingGuitar[lookupField]
    filteredGuitars = []
    for guitar in guitars:
        if guitar[lookupField] == criteria:
            filteredGuitars.append(guitar)
    return filteredGuitars

def get_guitar_recommendations(filterBy, media):
    spotifyID = media['spotify']
    spotifyID = spotifyID.replace("https://open.spotify.com/embed/track/", "")
    spotifyID = spotifyID.replace("?autoplay=1&controls=0&mute=0", "")
    guitarID = get_guitar_from_spotify_id(spotifyID)
    filters = {
        'shape':'bodyShape',
        'sound':'pickup',
        'brand':'brandName',
    }
    print(f"GuitarID: {guitarID} FilterBy: {filters[filterBy]}")
    guitars = get_guitars_with_matching(guitarID, filters[filterBy])
    print(guitars) 
    return guitars
