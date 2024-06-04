from django.urls import path
from .views import ClientListAPIView
from . import views



urlpatterns = [
    path('client-list/', ClientListAPIView.as_view()),
    path('price-filter/', views.ProductListFIlterPrice.as_view() ),
    path('brand-filter/', views.ProductListFIlterBrand.as_view()),
    path('ram-filter/', views.ProductListFIlterRAM.as_view() ),
    path('rom-filter/', views.ProductListFIlterROM.as_view()),
    path('batary-filter/', views.ProductListFIlterBATARY.as_view()),
      
]

