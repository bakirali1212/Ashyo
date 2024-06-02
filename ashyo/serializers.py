from rest_framework import serializers
from .models import  Category, Product, Brand,  AboutAshyo, Comment
import django_filters




class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('img',)


class AboutAshyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutAshyo
        fields = "__all__"

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"



