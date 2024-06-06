from rest_framework import serializers
from decimal import Decimal
from .models import  Category, Product, Brand,  AboutAshyo, Comment, Banner, Faq, Product, ProductImages, ProductInfoData
from .models import ProductInCart,Order,Comment



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
        'id', 
        'model',
        )

class CategorySerializer(serializers.ModelSerializer):
    product = serializers.ListSerializer(child=ProductSerializer(), source='category')

    class Meta:
        model = Category
        fields = (
        'id', 
        'name', 
        'product',
        )




class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
        'img',
        )


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
        exclude = (
        'created_at', 
        'id', 
        'updated_at',
        )

class RecommendationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = (
        'created_at', 
        'updated_at', 
        'icon',
        )

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = (
        'id', 
        'question'
        )
    

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = (
        'image_1', 
        'image_2', 
        'image_3'
        )

class ProductinfoDataserializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfoData
        fields = (
        'key', 
        'value'
        )

class Cammentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
        'id', 
        'text', 
        'rate'
        )

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImagesSerializer(many=True)
    features = ProductinfoDataserializer(many=True)
    monthly_payment = serializers.SerializerMethodField()
    comments = Cammentserializer(many=True)
    count_number_of_views = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name', 
            'img', 
            'images', 
            'price', 
            'monthly_payment', 
            'ram', 
            'rom', 
            'batary', 
            'delivery', 
            'features', 
            'comments', 
            'count_number_of_views'
        )
        ref_name = "ProductSerializer"

    def get_monthly_payment(self, obj):
        new_price = Decimal(obj.price) / 6 + Decimal(obj.price) * Decimal('0.018')
        return new_price
    
    def get_count_number_of_views(self, obj):
        request = self.context.get('request')
        if request:
            view_key = f"product_{obj.id}_views"
            if view_key not in request.session:
                request.session[view_key] = 1
            else:
                request.session[view_key] += 1
            return request.session[view_key]
        return 0

class ProductComparisonSerializer(serializers.ModelSerializer):
    features = ProductinfoDataserializer(many=True)
    category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        exclude = (
        'created_at', 
        'updated_at',
        )
    def get_category(self, obj):
        return obj.category.name


class MostpopularproductSerializer(serializers.ModelSerializer):
    count_number_of_views = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
        'id', 
        'name', 
        'img', 
        'price',
        'count_number_of_views'
        )
        ordering = ['-count_number_of_views']

    def get_count_number_of_views(self, obj):
        product_serializer = ProductSerializer(obj, context=self.context)
        return product_serializer.data.get('count_number_of_views')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = (
        'product', 
        'quantity', 
        'total_price'
        )

