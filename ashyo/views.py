from rest_framework.generics import ListAPIView
from rest_framework import generics
from .serializers import  CategoryListSerializer, ProductListSerializer, BrandListSerializer, AboutAshyoSerializer, CommentListSerializer
from .models import  Category, Product, Brand,  AboutAshyo, Comment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryListSerializer
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




