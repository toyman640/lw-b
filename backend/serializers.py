from rest_framework import serializers
from .models import CustomerUser, Category, Property, PropertyImage

class CustomerUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomerUser
    fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'means_of_id', 'avartar', 'is_active']
    read_only_fields = ['is_active']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name']


class PropertyImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = PropertyImage
    fields = ['image', 'description']

class PropertySerializer(serializers.ModelSerializer):
  images = PropertyImageSerializer(many=True, read_only=True)
  posted_by = serializers.StringRelatedField(read_only=True)

  class Meta:
    model = Property
    fields = ['id', 'title', 'price', 'country', 'state', 'area', 'category', 'description', 'posted_by', 'approved', 'images']
    read_only_fields = ['approved']