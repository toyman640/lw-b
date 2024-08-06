from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import update_last_login
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import api_view, permission_classes
from .models import CustomerUser, Category, Property
from .serializers import CustomerUserSerializer, CategorySerializer, PropertyImageSerializer, PropertySerializer
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
      user_serializer = CustomerUserSerializer(user)
      return Response({'user': user_serializer.data}, status=status.HTTP_200_OK)
    else:
      return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
  def post(self, request, *args, **kwargs):
    logout(request)
    return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
  user = request.user
  serializer = CustomerUserSerializer(user)
  return Response(serializer.data)

class CategoryListView(generics.ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [permissions.IsAuthenticated]

class CategoryCreateView(generics.CreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]



class PropertyCreateView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def post(self, request, *args, **kwargs):
    data = request.data
    images_data = data.pop('images', [])

    serializer = PropertySerializer(data=data)
    if serializer.is_valid():
      property_instance = serializer.save(posted_by=request.user)
      
      for image_data in images_data:
        image_serializer = PropertyImageSerializer(data=image_data)
        if image_serializer.is_valid():
          image_instance = image_serializer.save()
          property_instance.images.add(image_instance)

      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  permission_classes = [permissions.IsAuthenticated]

  def update(self, request, *args, **kwargs):
    if 'approved' in request.data and not request.user.is_superuser:
      raise PermissionDenied("Only superusers can change the 'approved' status.")
    return super().update(request, *args, **kwargs)

class PropertyListView(generics.ListAPIView):
  serializer_class = PropertySerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return Property.objects.filter(posted_by=self.request.user)


class ApprovedPropertyListView(generics.ListAPIView):
  queryset = Property.objects.filter(approved=True)
  serializer_class = PropertySerializer
  permission_classes = [permissions.IsAuthenticated]