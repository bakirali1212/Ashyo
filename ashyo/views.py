from rest_framework.generics import ListAPIView
from rest_framework import generics, status
from collections import defaultdict
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers



class CategorylistAPIView(ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.all().order_by('order')

class SendAplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.SendAplicationSerializer
    queryset = models.Client.objects.all()


class ProductListAPIView(ListAPIView):
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
    
class BrandListAPIView(ListAPIView):
    serializer_class = serializers.BrandListSerializer
    queryset = models.Brand.objects.all()



class ProductListFIlter(ListAPIView):
    serializer_class = serializers.ProductListserializerFilter
    queryset = models.Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'price',
        'brand__name',
        'ram',
        'rom',
        'batary',
    )

    
class CommentListAPIView(ListAPIView):
    serializer_class = serializers.CommentListSerializer
    queryset = models.Comment.objects.all()

class BannerListAPIView(ListAPIView):
    serializer_class = serializers.BannerListSerializer
    queryset = models.Banner.objects.all()

class RecommendationListAPIView(ListAPIView):
    serializer_class = serializers.RecommendationListSerializer
    queryset = models.Category.objects.all()

class FaqCreate(generics.CreateAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class MostpopularproductListAPIView(ListAPIView):
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

    
class FlialLocationListAPIView(ListAPIView):
    serializer_class = serializers.FlialLocationSerializer
    queryset = models.FlialLocation.objects.all()

class ClientdataCreatAPIView(generics.CreateAPIView):
    serializer_class = serializers.ClientdataSerializers
    queryset = models.Client.objects.all()