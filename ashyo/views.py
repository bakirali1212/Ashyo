from rest_framework import generics
from collections import defaultdict
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from django_filters import rest_framework as filters

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.serializers import ValidationError



class UserRegister(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data.get('phone')
        password = serializer.validated_data.get('password')
        if models.User.objects.filter(phone=phone, status='approved').exists():
            raise ValidationError(
                detail={"error": "Bunday foydalanuvchi ro'yxatdan o'tgan"},
                code=400
            )
        
        user = models.User.objects.filter(phone=phone)
        if user.exists():
            user = user.first()
        else:
            user = models.User.objects.create(phone=phone)
        user.set_password(password)
        code = random.randrange(1000, 9999)      #''.join[str(random.randint(1,9) for i in range(4) )]
        user.code = code
        user.expire_date = datetime.now() + timedelta(seconds=60)
        user.save()

        print(code)
        return Response(
            data={
                "user": user.id
            },
            status=201
            )
    

#     {
# "phone":"+998999999999",
# "password":"1"
# }
    
class VerifyAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = serializers.VerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')
        code = serializer.validated_data.get('code')

        if timezone.now() > user.expire_date or code != user.code:
            raise ValidationError(detail={
                "error":"voqt otib ketti yoki code xato"},
                status = 400
                )
        user.status = "approved"
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            data={
                'token':token.key,
                'user':user.id
            }
        )
    

class UserLogin(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginSerializer(data=request.data)

        phone = request.data.get('phone')
        password = request.data.get('password')

        user = authenticate(phone=phone, password=password)

        if user is None or user.status != "approved":
            raise ValidationError(detail={
                "error":"Siz ro'yxatdan o'tmagansiz"},
                code = 400
                )


        token, created = Token.objects.get_or_create(user=user)
        return Response(
            data={
                'token': token.key,
                'user': user.id
            }
        )

class CreditImageCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.CreditImageSerializer
    queryset = models.CreditImage.objects.all()

class CategorylistAPIView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class SendAplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.SendAplicationSerializer
    queryset = models.Client.objects.all()


class ProductListAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all()
    filter_backends =  [DjangoFilterBackend,SearchFilter]
    filterset_fields = ('category',)
    search_fields = ('name',)

class AboutAshyoAPIView(APIView):
    def get(self, request):
        queryset = models.AboutAshyo.objects.all()
        serializer = serializers.AboutAshyoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BrandImageListAPIView(generics.ListAPIView):
    serializer_class = serializers.BrandListSerializer
    queryset = models.Brand.objects.all()

class ProductFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = models.Product
        fields = ('price_min', 'price_max',)

class ProductListFIlterPrice(generics.ListAPIView):
    serializer_class = serializers.ProductPriceListserializerFilter
    queryset = models.Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    
class ProductListFIlter(generics.ListAPIView):
    serializer_class = serializers.ProductListserializerFilter
    queryset = models.Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'brand__name',
        'ram',
        'rom',
        'batary',
    )

class CommentListAPIView(generics.ListAPIView):
    serializer_class = serializers.CommentListSerializer
    queryset = models.Comment.objects.all()

class BannerListAPIView(generics.ListAPIView):
    serializer_class = serializers.BannerListSerializer
    queryset = models.Banner.objects.all()

class RecommendationListAPIView(generics.ListAPIView):
    serializer_class = serializers.RecommendationListSerializer
    queryset = models.Category.objects.all()

class FaqListCreate(generics.ListCreateAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class MostpopularproductListAPIView(generics.ListAPIView):
    serializer_class = serializers.MostpopularproductSerializer
    queryset = models.Product.objects.all()

class AddToCart(APIView):
    def post(self, request, pk, format=None):
        try:
            product = models.Product.objects.get(pk=pk)
        except models.Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)       
        data = {
            'product': product.id,
            'quantity': request.data.get('quantity', 1),  
            'total_price': product.price * int(request.data.get('quantity', 1))  
        }
        serializer = serializers.ProductInCartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceOrder(APIView):
    def get(self, request, format=None):
        cart_products = models.ProductInCart.objects.all()
        grouped_products = defaultdict(list)
        for cart_product in cart_products:
            grouped_products[cart_product.product.id].append(cart_product)
        cart_data = []
        for product_id, products in grouped_products.items():
            total_quantity = sum(product.quantity for product in products)
            total_price = sum(product.total_price for product in products)
            product_data = {
                'id': product_id,
                'name': products[0].product.name,
                'quantity': total_quantity,
                'total_price': total_price
            }
            cart_data.append(product_data)
        total_price = sum(product.total_price for product in cart_products)
        cart_data.append({'total_price': total_price})
        return Response(cart_data, status=status.HTTP_200_OK)

    
class FlialLocationListAPIView(generics.ListAPIView):
    serializer_class = serializers.FlialLocationSerializer
    queryset = models.FlialLocation.objects.all()

class ClientdataCreatAPIView(generics.CreateAPIView):
    serializer_class = serializers.ClientdataSerializers
    queryset = models.Client.objects.all()

class ArealistAPIView(generics.ListAPIView):
    serializer_class = serializers.Arealistserializers
    queryset = models.Tuman.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'region',
    )

class AreaCreatAPIView(generics.CreateAPIView):
    serializer_class = serializers.Arealistserializers
    queryset = models.Tuman.objects.all()


class BrandListAPIView(generics.ListAPIView):
    serializer_class = serializers.BrandListSerializers
    queryset = models.Brand.objects.all()

class RamListAPIView(generics.ListAPIView):
    serializer_class = serializers.RamListSerializer
    queryset = models.Product.objects.all()

class RomListAPIView(generics.ListAPIView):
    serializer_class = serializers.RomListSerializer
    queryset = models.Product.objects.all()

class BataryListAPIView(generics.ListAPIView):
    serializer_class = serializers.BataryistSerializer
    queryset = models.Product.objects.all()