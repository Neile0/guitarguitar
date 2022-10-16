from pstats import Stats
from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
import logic.data_retrieval as data_retrieval
import logic.filters as filters


# Create your views here.
@api_view(['GET'])
def guitars_with_songs(request):
    if request.method == 'GET':
        # response = {'content':'Hello World'}
        response = data_retrieval.get_guitars()
    return Response(response)
    
@api_view(['GET','POST'])
def youtube_spotify_pairs(request):
    if request.method == "GET":
        response = data_retrieval.get_youtube_spotify_pairs()
        return Response(response)
    if request.method == "POST":
        body = request.body
        data = {}
        try:
            data = json.loads(body)
            filterBy = data['type']
            media = data['media']
            guitars = filters.get_guitar_recommendations(filterBy, media)
            return Response(guitars, status=status.HTTP_200_OK)
        except:
            print("Cannot jsonify")
            return Response("", status=status.HTTP_406_NOT_ACCEPTABLE)
    
@api_view(['GET'])
def guitar_ids_with_3d_models(request):
    response = data_retrieval.get_guitar_ids_with_models()
    return Response(response)
