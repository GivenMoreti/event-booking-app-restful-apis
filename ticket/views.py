from django.shortcuts import render
from rest_framework import generics
from .serializer import TicketSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ticket


# Create your views here.
def getTickets(request):
    pass


#rest framework starts here

#Get All tickets
@api_view(['GET'])
def getTickets(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets,many=True)
    return Response(serializer.data)

#get individual ticket
@api_view(['GET'])
def getTicket(request,pk):
    existing_ticket = Ticket.objects.get(id=pk)
    serializer = TicketSerializer(existing_ticket,many=False)
    return Response(serializer.data)


#post event
@api_view(['POST'])
def createTicket(request):
    data = request.data
    new_event = Ticket.objects.create(
        body = data['body']
    )
    serializer = TicketSerializer(new_event,many=False)
    return Response(serializer.data)


#update event
@api_view(['PUT'])
def updateTicket(request,pk):
    data = request.data
    ticket = Ticket.objects.get(id =pk)
    serializer = TicketSerializer(ticket,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

#delete an event
@api_view(['DELETE'])
def deleteTicket(request,pk):
    data = Ticket.objects.get(id=pk)
    data.delete()
    return Response("ticket was deleted")