from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


# Create your views here.
@api_view(['GET'])
def guitars_with_songs(request):
    if request.method == 'GET':
        # response = {'content':'Hello World'}
        response = requests.get('http://services.guitarguitar.co.uk/WebService/api/hackathon/guitarswithsongs')
    return Response(response)
    
