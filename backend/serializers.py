from rest_framework import serializers
from .models import CustomerUser

class CustomerUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomerUser
    fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'means_of_id', 'avartar', 'is_active']
    read_only_fields = ['is_active']
