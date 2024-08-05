from django.urls import path
from .views import current_user_view, CustomerUserListView, CustomerUserCreateView, CustomerUserDetailView, LoginView, LogoutView, CategoryListView, CategoryCreateView

urlpatterns = [
  path('current-user/', current_user_view, name='current-user'),
  path('customers/', CustomerUserListView.as_view(), name='customer-list'),
  path('customers/create/', CustomerUserCreateView.as_view(), name='customer-create'),
  path('customers/<int:pk>/', CustomerUserDetailView.as_view(), name='customer-detail'),
  path('categories/', CategoryListView.as_view(), name='category-list'),
  path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
]
