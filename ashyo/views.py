from rest_framework.generics import ListAPIView
from rest_framework import generics
from .serializers import  ProductListSerializer, BrandListSerializer, ProductListserializerFilter
from .models import Client, Category, Product, Brand,  AboutAshyo, Comment
from .serializers import  CategorySerializer, ProductListSerializer, BrandListSerializer, AboutAshyoSerializer, CommentListSerializer, ClientdataSerializers
from .models import  Category, Product, Brand,  AboutAshyo, Comment, Client
from .serializers import   ProductListSerializer, BrandListSerializer, AboutAshyoSerializer, CommentListSerializer,BannerListSerializer
from .serializers import RecommendationListSerializer, FaqSerializer, ProductSerializer, ProductInCartSerializer, OrderSerializer,FlialLocationSerializer
from .models import  Category, Product, Brand,  AboutAshyo, Comment, Banner, Faq,FlialLocation
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategorylistAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()




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



class ProductListFIlterPrice(ListAPIView):
    serializer_class = ProductListserializerFilter
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'price',
    )

class ProductListFIlterBrand(ListAPIView):
    serializer_class = ProductListserializerFilter
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'brand__name',
    )

class ProductListFIlterRAM(ListAPIView):
    serializer_class = ProductListserializerFilter
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'ram',
    )

class ProductListFIlterROM(ListAPIView):
    serializer_class = ProductListserializerFilter
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'rom',
    )

class ProductListFIlterBATARY(ListAPIView):
    serializer_class = ProductListserializerFilter
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
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

class AddToCart(APIView):
    def post(self, request):
        serializer = ProductInCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaceOrder(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FlialLocationListAPIView(ListAPIView):
    serializer_class = FlialLocationSerializer
    queryset = FlialLocation.objects.all()

class ClientdataCreatAPIView(generics.CreateAPIView):
    serializer_class = ClientdataSerializers
    queryset = Client.objects.all()