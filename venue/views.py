from django.shortcuts import render
from rest_framework import generics
from .serializer import VenueSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Venue


# Create your views here.
def getTickets(request):
    pass


#rest framework starts here

#Get All venues
@api_view(['GET'])
def getVenues(request):
    venues = Venue.objects.all()
    serializer = VenueSerializer(venues,many=True)
    return Response(serializer.data)

#get individual ticket
@api_view(['GET'])
def getVenue(request,pk):
    existing_venue = Venue.objects.get(id=pk)
    serializer = VenueSerializer(existing_venue,many=False)
    return Response(serializer.data)


#post venue
@api_view(['POST'])
def createVenue(request):
    data = request.data
    new_venue = Venue.objects.create(
        body = data['body']
    )
    serializer = VenueSerializer(new_venue,many=False)
    return Response(serializer.data)


#update event
@api_view(['PUT'])
def updateVenue(request,pk):
    data = request.data
    venue = Venue.objects.get(id =pk)
    serializer = VenueSerializer(venue,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

#delete a venue
@api_view(['DELETE'])
def deleteVenue(request,pk):
    data = Venue.objects.get(id=pk)
    data.delete()
    return Response("venue was deleted")