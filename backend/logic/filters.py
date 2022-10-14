from data_retrieval import get_guitars_with_songs

anID = "7BsPyswBtiM1PbPnUnuNzE?si=93175f88875b4d3c"
aUrl = "https://www.youtube.com/watch?v=qjEqt_cpey8"

def get_guitar_from_spotify_id(id):
    data = get_guitars_with_songs()
    for guitar in data:
        if id == guitar['spotifyId']:
            return guitar['skU_ID']
    return False
    
def get_guitar_from_youtube(url):
    data = get_guitars_with_songs()
    for guitar in data: 
        if url == guitar['youtubeUrl']:
            return guitar['skU_ID']
    return False 
