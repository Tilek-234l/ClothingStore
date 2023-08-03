from rest_framework import serializers
from .models import User, Product


class UserSerializer(serializers.ModelSerializer):
    favorite_products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'favorite_products')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
