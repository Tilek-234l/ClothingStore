from rest_framework import serializers
from .models import User, Product


class UserSerializer(serializers.ModelSerializer):
    favorite_products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'favorite_products')
        extra_kwargs = {
            'password': {'write_only': True},  # Пароль не будет отображаться при сериализации
            'email': {'required': True}  # Добавлено, чтобы убедиться, что email указан при создании/обновлении
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
