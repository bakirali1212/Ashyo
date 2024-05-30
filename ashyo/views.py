from rest_framework.generics import ListAPIView
from rest_framework import generics
from .serializers import ClientSerializer
from .models import Client, Category, Characteristics, Product, Brand, ProductMemory, ProductImages, AboutAshyo, Comment, ProductInCart
from django_filters.rest_framework import DjangoFilterBackend

class ClientListAPIView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()