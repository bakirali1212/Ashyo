from rest_framework import serializers
from decimal import Decimal
from .models import  Category, Product, Brand,  AboutAshyo, Comment, Banner, Faq, Product, ProductImages, ProductInfoData
from .models import ProductInCart,Order,Comment, Address
from .models import ProductInCart,Order,FlialLocation,Client
from .models import ProductInCart,Order,Comment, CreditImage
from . import models


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
        fields = (
        'img',
        )

class BrandFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields  = (
            "id",
            'name',
            "img",
            )

class ProductListserializerFilter(serializers.ModelSerializer):
    brand = BrandFilterSerializer(many =True)
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
        exclude = (
        "created_at",
        "updated_at"
        )

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
        fields = ('image_1', 'image_2', 'image_3')

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
        
    



class ProductInCartSerializer(serializers.ModelSerializer):
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





        

class FlialLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlialLocation
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = ['product', 'quantity', 'total_price']

class Addressserializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
        "longitude",
        "latitude",
        )

class Productclientdataserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
        "id",
        "name"
        )


class CreditImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditImage
        fields = (
            "image_1",
            "image_2",
        )

class ClientdataSerializers(serializers.ModelSerializer):
    lat = serializers.FloatField(required=True, write_only=True)
    lon = serializers.FloatField(required=True, write_only=True)

    class Meta:
        model = Client
        fields = (
        "first_name",
        "last_name",
        "phone",
        "product_count",
        'lat',
        'lon',
        )
    

    def create(self, validate_data):
        lat = validate_data.pop('lat', 0)
        lon = validate_data.pop('lon', 0)
        address = Address.objects.create(longitude=lon, latitude=lat)
        validate_data['address'] = address
        instance = super().create(validate_data)
        return instance


class FlialLocationCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FlialLocation
        fields = (
        "title",
        "longitude",
        "latitude",
        )

class UserSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()

class VerifySerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset= models.User.objects.filter(status="new"))
    code = serializers.CharField()


class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.User
        fields = (
            'phone',
            'password',
        )