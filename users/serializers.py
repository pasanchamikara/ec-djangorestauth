from rest_framework import serializers
from .models import User, Customer

class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField()
    contact_no = serializers.CharField(max_length=50)

    class Meta:
        model = User

class CustomerSerializer(serializers.ModelSerializer):
    customer_id = serializers.UUIDField()
    special_notes = serializers.CharField(max_length=255)

    class Meta:
        model = Customer