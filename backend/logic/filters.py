from data_retrieval import get_guitars_with_songs, get_guitars, get_guitar

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
    searchingGuitar = get_guitar(guitarID)
    criteria = searchingGuitar[lookupField]
    filteredGuitars = []
    for guitar in guitars:
        if guitar[lookupField] == criteria:
            filteredGuitars.append(guitar)
    return filteredGuitars

if __name__ == "__main__":
    print(get_guitars_with_matching(aGuitarId, 'bodyShape'))