# products/urls.py

from django.urls import path
from .views import UserListCreateView, ProductListView, ProductDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
