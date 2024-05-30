from rest_framework.generics import ListAPIView
from rest_framework import generics
from .serializers import KategotiyaSerializer
from .models import Kategoriya, Mahsulot, FoydalanuvchiMalumot, Buyurtma, BuyurtmaItem, YetkazibBerishManzil, YagonaSahifa
from django_filters.rest_framework import DjangoFilterBackend

class KategoriyaListAPIView(ListAPIView):
    serializer_class = KategotiyaSerializer
    queryset = Kategoriya.objects.all()