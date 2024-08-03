from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import CustomerUser
from .serializers import CustomerUserSerializer

class CustomerUserListView(generics.ListAPIView):
  queryset = CustomerUser.objects.all()
  serializer_class = CustomerUserSerializer

class CustomerUserCreateView(APIView):
    
  def post(self, request, *args, **kwargs):
    serializer = CustomerUserSerializer(data=request.data)
    
    if serializer.is_valid():
      serializer.save(is_active=False)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IsSuperUser(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user and request.user.is_superuser

class CustomerUserDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = CustomerUser.objects.all()
  serializer_class = CustomerUserSerializer

  def update(self, request, *args, **kwargs):
    if 'is_active' in request.data and not request.user.is_superuser:
      raise PermissionDenied("Only superusers can change the 'is_active' status.")
    return super().update(request, *args, **kwargs)
