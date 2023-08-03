from drf_yasg.openapi import Response
from rest_framework import generics, mixins
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddToFavoritesView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        # Выполняем добавление товара в избранное без запроса пароля
        user = request.user
        product_id = self.kwargs['pk']
        product = Product.objects.get(pk=product_id)
        user.favorite_products.add(product)

        serializer = self.get_serializer(user)
        return Response(serializer.data)


class RemoveFromFavoritesView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        # Выполняем удаление товара из избранного
        user = self.request.user
        product_id = self.kwargs['pk']
        product = Product.objects.get(pk=product_id)
        user.favorites.remove(product)
        return self.destroy(request, *args, **kwargs)


class AddProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer