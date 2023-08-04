from django.urls import path
from .views import UserListCreateView, ProductListView, ProductDetailView, RemoveFromFavoritesView, AddProductView, DeleteProductView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/add-to-favorites/', RemoveFromFavoritesView.as_view(), name='add-to-favorites'),
    path('products/add/', AddProductView.as_view(), name='add-product'),
    path('products/<int:pk>/delete/', DeleteProductView.as_view(), name='delete-product'),
]
