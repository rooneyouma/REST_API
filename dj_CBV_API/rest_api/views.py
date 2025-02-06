from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer


class ItemList(APIView):

    def get(self,request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ItemDetail(APIView):

    def get_item(self,id):
        try:
            return Item.objects.get(id=id)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,id):
        item = self.get_item(id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    def put(self,request,id):
        item = self.get_item(id)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        item = self.get_item(id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)