from django.urls import path
from . import views
from .views import  ProductListAPIView, AboutAshyoAPIView, BrandListAPIView, CommentListAPIView
from .views import RecommendationListAPIView, FaqListCreate, ProductDetailView, AddToCart, PlaceOrder
from .views import BannerListAPIView
from .views import CategorylistAPIView, ProductListAPIView, AboutAshyoAPIView, BrandListAPIView, CommentListAPIView,FlialLocationListAPIView, ClientdataCreatAPIView





urlpatterns = [
    path('price-filter/', views.ProductListFIlterPrice.as_view() ),
    path('brand-filter/', views.ProductListFIlterBrand.as_view()),
    path('ram-filter/', views.ProductListFIlterRAM.as_view() ),
    path('rom-filter/', views.ProductListFIlterROM.as_view()),
    path('batary-filter/', views.ProductListFIlterBATARY.as_view()),
    path('category/', CategorylistAPIView.as_view()),    
    path('about-ashyo/', AboutAshyoAPIView.as_view()),
    path('brand-list/', BrandListAPIView.as_view()),
    path('comment-list/', CommentListAPIView.as_view()),
    path('banner-list/', BannerListAPIView.as_view()),
    path('recommendation-list/', RecommendationListAPIView.as_view()),
    path('faqs/', FaqListCreate.as_view()),
    path('product-detail/<int:pk>/', ProductDetailView.as_view()),
    path('add-to-cart/', AddToCart.as_view()),
    path('place-order/', PlaceOrder.as_view()),
    path('send-aplicationns/', views.SendAplicationCreateAPIView.as_view()),
    
    path('product/', ProductListAPIView.as_view()),
    path('Flial-list/', FlialLocationListAPIView.as_view()), 
    path('client-date/', ClientdataCreatAPIView.as_view()),   

      
]

