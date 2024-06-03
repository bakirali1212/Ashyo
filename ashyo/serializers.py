from rest_framework import serializers
from decimal import Decimal
from .models import  Category, Product, Brand,  AboutAshyo, Comment, Banner, Faq, Product, ProductImages, ProductInfoData
from .models import ProductInCart,Order
import django_filters



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'model']

class CategorySerializer(serializers.ModelSerializer):
    product = serializers.ListSerializer(child=ProductSerializer(), source='category')

    class Meta:
        model = Category
        fields = ['id', 'name', 'product']




class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('img',)


class AboutAshyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutAshyo
        fields = "__all__"

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"



class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        exclude = ('created_at', 'id', 'updated_at',)

class RecommendationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at', 'updated_at', 'icon',)

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'question']
    

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image_1', 'image_2', 'image_3']

class ProductinfoDataserializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfoData
        fields = ['key', 'value']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True)
    features = ProductinfoDataserializer(many=True)
    monthly_payment = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'img', 'images', 'price', 'monthly_payment', 'ram', 'rom', 'batary', 'delivery', 'features']
        ref_name = "ProductSerializer"

    def get_monthly_payment(self, obj):
        new_price = Decimal(obj.price) / 6 + Decimal(obj.price) * Decimal('0.018')
        return new_price

class ProductComparisonSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)




class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
