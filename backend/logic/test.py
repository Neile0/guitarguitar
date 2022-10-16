import requests

endpoint = "http://localhost:8000/api/3d-models/"
aJson = {"type":"brand","media":{"youtube":"https://www.youtube.com/embed/pAgnJDJN4VA" , "spotify":"https://open.spotify.com/embed/track/08mG3Y1vljYA6bvDt4Wqkj?si=fd4b4b4efce64148?autoplay=1&controls=0&mute=0" }} 

r = requests.get(endpoint)

print(r.json())