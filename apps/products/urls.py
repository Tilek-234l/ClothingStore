from django.urls import path
from .views import UserListCreateView, ProductListView,\
    ProductDetailView, \
    RemoveFromFavoritesView, AddProductView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('products-list/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('removefavorite/', RemoveFromFavoritesView.as_view(), name='remove-favorite'),
    path('add/', AddProductView.as_view(), name='add-product'),

]
