from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import logic.data_retrieval as data_retrieval


# Create your views here.
@api_view(['GET'])
def guitars_with_songs(request):
    if request.method == 'GET':
        # response = {'content':'Hello World'}
        response = data_retrieval.get_guitars()
    return Response(response)
    
@api_view(['GET'])
def youtube_spotify_pairs(request):
    response = data_retrieval.get_youtube_spotify_pairs()
    return Response(response)