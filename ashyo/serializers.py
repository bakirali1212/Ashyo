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
        fields = "__all__"

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
    images = ProductImagesSerializer(many=True)
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
        term_payment = models.TermPayment.objects.filter(product=obj).first()
        if term_payment:
            monthly_payment = (Decimal(obj.price) * (1 + Decimal(term_payment.percentage) / 100)) / term_payment.month
            return monthly_payment
        return None

    def get_count_number_of_views(self, obj):
        request = self.context.get('request')
        if request:
            view_key = f"product_{obj.id}_views"
        if view_key not in request.session:
            request.session[view_key] = 1
        else:
            request.session[view_key] += 1
            obj.count_number_of_views = request.session[view_key]
            obj.save() 
            return obj.count_number_of_views
        return 0
    


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

    def get_count_number_of_views(self, obj):
        return obj.count_number_of_views



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

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"

class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductInCart
        fields = ['product', 'quantity', 'total_price']

class Addressserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = (
        "longitude",
        "latitude",
        )

class Productclientdataserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
        "id",
        "name"
        )

class ClientdataSerializers(serializers.ModelSerializer):
    lat = serializers.FloatField(required=True, write_only=True)
    lon = serializers.FloatField(required=True, write_only=True)
   
    class Meta:
        model = models.Client
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
        address = models.Address.objects.create(longitude=lon, latitude=lat)
        validate_data['address'] = address
        instance = super().create(validate_data)
        return instance

    
        fields = (
        'product', 
        'quantity', 
        'total_price'
        )