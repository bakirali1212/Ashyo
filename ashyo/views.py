from rest_framework.generics import ListAPIView
from rest_framework import generics
from .serializers import  CategorySerializer, ProductListSerializer, BrandListSerializer, AboutAshyoSerializer, CommentListSerializer
from .models import  Category, Product, Brand,  AboutAshyo, Comment
from .serializers import   ProductListSerializer, BrandListSerializer, AboutAshyoSerializer, CommentListSerializer,BannerListSerializer, MostpopularproductSerializer
from .serializers import RecommendationListSerializer, FaqSerializer, ProductSerializer, ProductInCartSerializer, OrderSerializer
from .models import  Category, Product, Brand,  AboutAshyo, Comment, Banner, Faq, ProductInCart
from collections import defaultdict
from .serializers import  ProductListSerializer, BrandListSerializer, ProductListserializerFilter
from .models import Client, Category, Product, Brand,  AboutAshyo, Comment
from .serializers import  CategorySerializer, ProductListSerializer, BrandListSerializer, AboutAshyoSerializer, CommentListSerializer
from .models import  Category, Product, Brand,  AboutAshyo, Comment
from .serializers import   ProductListSerializer, BrandListSerializer, AboutAshyoSerializer, CommentListSerializer,BannerListSerializer
from .serializers import RecommendationListSerializer, FaqSerializer, ProductSerializer, ProductInCartSerializer, OrderSerializer,FlialLocationSerializer
from .models import  Category, Product, Brand,  AboutAshyo, Comment, Banner, Faq,FlialLocation
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers


class CategorylistAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class SendAplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.SendAplicationSerializer
    queryset = models.Client.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    filter_backends =  [DjangoFilterBackend,SearchFilter]
    filterset_fields = ('category',)
    search_fields = ('name',)

class AboutAshyoAPIView(APIView):
    def get(self, request):
        queryset = AboutAshyo.objects.all()
        serializer = AboutAshyoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BrandListAPIView(ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()



class ProductListFIlter(ListAPIView):
    serializer_class = ProductListserializerFilter
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'price',
        'brand__name',
        'ram',
        'rom',
        'batary',
    )

    
class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()

class BannerListAPIView(ListAPIView):
    serializer_class = BannerListSerializer
    queryset = Banner.objects.all()

class RecommendationListAPIView(ListAPIView):
    serializer_class = RecommendationListSerializer
    queryset = Category.objects.all()

class FaqListCreate(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MostpopularproductListAPIView(ListAPIView):
    serializer_class = MostpopularproductSerializer
    queryset = Product.objects.all()

class AddToCart(APIView):
    def post(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)       
        data = {
            'product': product.id,
            'quantity': request.data.get('quantity', 1),  
            'total_price': product.price * int(request.data.get('quantity', 1))  
        }
        serializer = ProductInCartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceOrder(APIView):
    def get(self, request, format=None):
        cart_products = ProductInCart.objects.all()
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

    
class FlialLocationListAPIView(ListAPIView):
    serializer_class = FlialLocationSerializer
    queryset = FlialLocation.objects.all()

class ClientdataCreatAPIView(generics.CreateAPIView):
    serializer_class = serializers.ClientdataSerializers
    queryset = Client.objects.all()