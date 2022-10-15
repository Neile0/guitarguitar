import requests

endpoint = "http://localhost:8000/api/media/"
aJson = {"type":"brand","media":{"youtube":"https://www.youtube.com/embed/pAgnJDJN4VA" , "spotify":"https://open.spotify.com/embed/track/08mG3Y1vljYA6bvDt4Wqkj?si=fd4b4b4efce64148?autoplay=1&controls=0&mute=0" }} 

requests.post(endpoint, json=aJson)