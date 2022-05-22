from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['title', 'description']

    def create(self, validated_data):
        return super().create(validated_data)


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for position in positions:
            product = StockProduct(stock=stock, **position)
            product.save()
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        st = StockProduct.objects.filter(stock=stock)
        for position in positions:
            product = position.pop('product')
            quantity = position.pop('quantity')
            price = position.pop('price')
            updated_values = {'quantity': quantity, 'price': price}
            st.update_or_create(stock=stock, product=product, defaults=updated_values)
        return stock
