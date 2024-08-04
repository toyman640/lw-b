from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import update_last_login
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import CustomerUser
from .serializers import CustomerUserSerializer
from rest_framework.authtoken.models import Token

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


class LoginView(APIView):
  permission_classes = [AllowAny]

  def post(self, request, *args, **kwargs):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      update_last_login(None, user)
      return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
    else:
      return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
  def post(self, request, *args, **kwargs):
    logout(request)
    return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
