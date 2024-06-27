from django.shortcuts import render
from rest_framework import generics
from .serializer import EventSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event


# Create your views here.
def getEvents(request):
    pass


#rest framework starts here

#Get All events
@api_view(['GET'])
def getEvents(request):
    artist = Event.objects.all()
    serializer = EventSerializer(artist,many=True)
    return Response(serializer.data)

#get individual event
@api_view(['GET'])
def getEvent(request,pk):
    existing_event = Event.objects.get(id=pk)
    serializer = EventSerializer(existing_event,many=False)
    return Response(serializer.data)


#post event
@api_view(['POST'])
def createEvent(request):
    data = request.data
    new_event = Event.objects.create(
        body = data['body']
    )
    serializer = EventSerializer(new_event,many=False)
    return Response(serializer.data)


#update event
@api_view(['PUT'])
def updateEvent(request,pk):
    data = request.data
    event = Event.objects.get(id =pk)
    serializer = EventSerializer(event,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

#delete an event
@api_view(['DELETE'])
def deleteEvent(request,pk):
    data = Event.objects.get(id=pk)
    data.delete()
    return Response("event was deleted")