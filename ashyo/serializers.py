from rest_framework import serializers
from decimal import Decimal
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
        'id', 
        'model',
        )
       

class CategorySerializer(serializers.ModelSerializer):
    product = serializers.ListSerializer(child=ProductSerializer(), source='category')

    class Meta:
        model = models.Category
        fields = (
        'id', 
        'name', 
        'product',
        )

class SendAplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = (
            "first_name",
            "last_name",
            'phone',
            'email',
            'text',
        )


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            'name',
            'img',
            'price',
            )

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = (
        'img',
        )

class BrandFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields  = (
            "id",
            'name',
            "img",
            )

class ProductListserializerFilter(serializers.ModelSerializer):
    brand = BrandFilterSerializer(many =True)
    class Meta:
        model = models.Product
        fields = (
            'name',
            'price',
            'img',
            'ram',
            'rom',
            'batary',
            'brand',
        )

class ProductPriceListserializerFilter(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            'name',
            'price',
            'img',
            'ram',
            'rom',
            'batary',
            
        )


class AboutAshyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutAshyo
        exclude = (
        "created_at",
        "updated_at"
        )

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"



class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        exclude = (
        'created_at', 
        'id', 
        'updated_at',
        )

class RecommendationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        exclude = (
        'created_at', 
        'updated_at', 
        'icon',
        )

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faq
        fields = (
        'id', 
        'question'
        )
    

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImages
        fields = (
        'image_1', 
        'image_2', 
        'image_3'
        )
        fields = ('image_1', 'image_2', 'image_3')

class ProductinfoDataserializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductInfoData
        fields = (
        'key', 
        'value'
        )

class Cammentserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
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
        model = models.Product
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
        model = models.Product
        exclude = (
        'created_at', 
        'updated_at',
        )
    def get_category(self, obj):
        return obj.category.name


class MostpopularproductSerializer(serializers.ModelSerializer):
    count_number_of_views = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
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
        model = models.Product
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
        model = models.FlialLocation
        fields = '__all__'



class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductInCart
        fields = ['product', 'quantity', 'total_price']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ['id', 'name']

class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tuman
        fields = ['id', 'name', 'region']

class Arealistserializers(serializers.ModelSerializer):
    region = RegionSerializer(many = True,read_only=True)
    class Meta:
        model = models.Tuman
        fields = (
            "name",
            "region",
            )

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShippingAddress
        fields = ['id', 'region', 'tuman', 'address']

class Pymenserializer(serializers.ModelSerializer):
    class Meta:
        model = models.PymentType
        fields = "__all__"

class ClientdataSerializers(serializers.ModelSerializer):
    shipping_address = ShippingAddressSerializer(read_only=True)
    class Meta:
        model = models.Client
        fields = (
        "first_name",
        "last_name",
        "pyment",
        "phone", 
        'shipping_address',

        )
    def create(self, validated_data):
        shipping_address_data = validated_data.pop('shipping_address')
        shipping_address = models.ShippingAddress.objects.create(**shipping_address_data)
        client = models.Client.objects.create(shipping_address=shipping_address, **validated_data)
        return client

    def create(self, validate_data):
        instance = super().create(validate_data)
        return instance



class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = (
            'name',
            )
        
class RamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            'ram',
            )
        
class RomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            'rom',
            )
        
class BataryistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            'batary',
            )