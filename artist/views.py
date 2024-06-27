from django.shortcuts import render
from .models import Artist

#student api dependencies
from rest_framework import generics
from .serializer import ArtistSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

def getArtists(request):
    pass


#rest framework starts here

#Get All artists
@api_view(['GET'])
def getArtists(request):
    artist = Artist.objects.all()
    serializer = ArtistSerializer(artist,many=True)
    return Response(serializer.data)

#get individual artist
@api_view(['GET'])
def getArtist(request,pk):
    existing_artist = Artist.objects.get(id=pk)
    serializer = ArtistSerializer(existing_artist,many=False)
    return Response(serializer.data)


#post artist
@api_view(['POST'])
def createArtist(request):
    data = request.data
    new_artist = Artist.objects.create(
        body = data['body']
    )
    serializer = ArtistSerializer(new_artist,many=False)
    return Response(serializer.data)


#update artist
@api_view(['PUT'])
def updateArtist(request,pk):
    data = request.data
    artist = Artist.objects.get(id =pk)
    serializer = ArtistSerializer(artist,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

#delete an artist
@api_view(['DELETE'])
def deleteArtist(request,pk):
    data = Artist.objects.get(id=pk)
    data.delete()
    return Response("artist was deleted")