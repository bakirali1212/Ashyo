from rest_framework import serializers
from decimal import Decimal
from .models import  Category, Product, Brand,  AboutAshyo, Comment, Banner, Faq, Product, ProductImages, ProductInfoData
from .models import ProductInCart,Order,FlialLocation,Client



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

class SendAplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = (
            "first_name",
            "last_name",
            'phone',
            'email',
            'text',
        )


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('img',)

class BrandFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields  = ('name',)

class ProductListserializerFilter(serializers.ModelSerializer):
    brand = BrandFilterSerializer()
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'img',
            'ram',
            'rom',
            'batary',
            'brand',

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
    features = ProductinfoDataserializer(many=True, read_only=True)
    price_discounted = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
                'id',
                'name',
                'img',
                'price',
                'price_discounted',
                'ram',
                'rom',
                'batary',
                'delivery',
                'features',
                )
        
        ref_name = "ProductSerializer"
    def get_price_discounted(self, obj):
        if obj.price > Decimal('100'):
            return obj.price * Decimal('0.05')  
        else:
            return obj.price


class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = "__all__"


        

class FlialLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlialLocation
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class ClientdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ("email",)
