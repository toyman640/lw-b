from django.urls import path
from .views import CustomerUserListView, CustomerUserCreateView, CustomerUserDetailView, LoginView, LogoutView

urlpatterns = [
  path('customers/', CustomerUserListView.as_view(), name='customer-list'),
  path('customers/create/', CustomerUserCreateView.as_view(), name='customer-create'),
  path('customers/<int:pk>/', CustomerUserDetailView.as_view(), name='customer-detail'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
]
