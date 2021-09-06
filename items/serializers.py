from typing import ItemsView
from django.db import models
from rest_framework import fields, serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    price = serializers.FloatField()

    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return instance