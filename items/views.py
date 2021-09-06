from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from rest_framework import status

from django.http import Http404
from .models import Item
from .serializers import ItemSerializer
from rest_framework.parsers import JSONParser 

# Create your views here.
class ItemAPIView(APIView):
    def get(self, request, format=None):
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        print("seri")
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemParamAPIView(APIView):
    def get_object(self, id):
        try:
            return Item.objects.get(item_id=id)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Item = self.get_object(id)
        serializer = ItemSerializer(Item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Item = self.get_object(id)
        serializer = ItemSerializer(Item, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Item = self.get_object(id)
        Item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)