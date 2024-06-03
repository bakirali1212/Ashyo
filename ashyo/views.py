from rest_framework.generics import ListAPIView
from rest_framework import generics
from .serializers import  CategorySerializer, ProductListSerializer, BrandListSerializer, AboutAshyoSerializer, CommentListSerializer
from .models import  Category, Product, Brand,  AboutAshyo, Comment
from .serializers import   ProductListSerializer, BrandListSerializer, AboutAshyoSerializer, CommentListSerializer,BannerListSerializer
from .serializers import RecommendationListSerializer, FaqSerializer, ProductSerializer,SendAddressSerializer, ProductInCartSerializer, OrderSerializer,FlialLocationSerializer
from .models import  Category, Product, Brand,  AboutAshyo, Comment, Banner, Faq, Address,FlialLocation
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategorylistAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

class AboutAshyoAPIView(APIView):
    def get(self, request):
        queryset = AboutAshyo.objects.all()
        serializer = AboutAshyoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BrandListAPIView(ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()
    
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

class SendAddressCreatAPIView(generics.CreateAPIView):
    serializer_class = SendAddressSerializer
    queryset = Address.objects.all()