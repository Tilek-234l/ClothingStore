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

# Наследуемся от AllowAny для отключения аутентификации
class AddToFavoritesView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        # Выполняем добавление товара в избранное без запроса пароля
        user = self.request.user
        product_id = self.kwargs['pk']
        product = Product.objects.get(pk=product_id)
        user.favorites.add(product)
        return self.create(request, *args, **kwargs)
