from rest_framework import serializers
from .models import Client, Category, Characteristics, Product, Brand, ProductMemory, ProductImages, AboutAshyo, Comment, ProductInCart, Order
import django_filters

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"