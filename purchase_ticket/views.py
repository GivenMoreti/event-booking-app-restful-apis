from django.shortcuts import render
from rest_framework import generics
from .serializer import PurchaseSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Purchase


# Create your views here.
def getPurchase(request):
    pass


#rest framework starts here

#Get All tickets
@api_view(['GET'])
def getPurchases(request):
    purchases = Purchase.objects.all()
    serializer = PurchaseSerializer(purchases,many=True)
    return Response(serializer.data)

#get individual event
@api_view(['GET'])
def getPurchase(request,pk):
    existing_purchase = Purchase.objects.get(id=pk)
    serializer = PurchaseSerializer(existing_purchase,many=False)
    return Response(serializer.data)


#post event
@api_view(['POST'])
def createPurchase(request):
    data = request.data
    new_purchase = Purchase.objects.create(
        body = data['body']
    )
    serializer = PurchaseSerializer(new_purchase,many=False)
    return Response(serializer.data)


#update purchase
@api_view(['PUT'])
def updatePurchase(request,pk):
    data = request.data
    purchase = Purchase.objects.get(id =pk)
    serializer = PurchaseSerializer(purchase,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

#delete a purchase
@api_view(['DELETE'])
def deletePurchase(request,pk):
    data = Purchase.objects.get(id=pk)
    data.delete()
    return Response("purchase was deleted")