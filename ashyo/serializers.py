from rest_framework import serializers
from .models import Kategoriya, Mahsulot, FoydalanuvchiMalumot, Buyurtma, BuyurtmaItem, YetkazibBerishManzil, YagonaSahifa
import django_filters

class KategotiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoriya
        fields = "__all__"