from rest_framework.generics import ListAPIView
from rest_framework import generics
from .serializers import ClientListSerializer, CategoryListSerializer, ProductListSerializer, BrandListSerializer
from .serializers import ProductMemoryListSerializer,ProductImagesListSerializer
from .models import Client, Category, Product, Brand, ProductMemory, ProductImages, AboutAshyo, Comment, ProductInCart
from django_filters.rest_framework import DjangoFilterBackend

class ClientListAPIView(ListAPIView):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()

class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

class BrandListAPIView(ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()



class productMemoryListAPIView(ListAPIView):
    serializer_class = ProductMemoryListSerializer
    queryset = ProductMemory.objects.all()

