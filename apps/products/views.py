from drf_yasg.openapi import Response
from rest_framework import generics, mixins, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import User, Product
from .serializers import UserSerializer, ProductSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import status
from rest_framework.response import Response


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
        """
        Добавляет товар в список избранных для пользователя.
        """
        user = request.user
        product_id = self.kwargs['pk']
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Продукт не найден."}, status=status.HTTP_404_NOT_FOUND)

        user.favorite_products.add(product)

        serializer = self.get_serializer(user)
        return Response(serializer.data)


class RemoveFromFavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk=None):
        """
        Удаляет товар из списка избранных для пользователя.
        """
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"detail": "Продукт не найден."}, status=status.HTTP_404_NOT_FOUND)

        user = request.user
        if product in user.favorite_products.all():
            user.favorite_products.remove(product)
            return Response({"message": "Продукт удален из избранного."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Продукт не был в избранном."}, status=status.HTTP_400_BAD_REQUEST)


class AddProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        """
        Удаляет товар.
        """
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
