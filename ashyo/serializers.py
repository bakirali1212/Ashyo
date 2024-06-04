from rest_framework import serializers
from .models import Client, Category, Product, Brand, ProductMemory, ProductImages, AboutAshyo, Comment, ProductInCart, Order
import django_filters


     # All List serializers!!!
class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class BrandFilterSeruializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        field = (
            "name",
        )


class ProductListserializerFilter(serializers.ModelSerializer):
    brand = BrandFilterSeruializer()
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'image',
            'ram',
            'rom',
            'batary',
            'brand',

        )




class ProductMemoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMemory
        fields = "__all__"

class ProductImagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"

class AboutAshyoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutAshyo
        fields = "__all__"

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ProductInCartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = "__all__"

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"