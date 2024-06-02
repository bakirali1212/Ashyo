from django.urls import path
from .views import  ProductListAPIView, AboutAshyoAPIView, BrandListAPIView, CommentListAPIView
from .views import RecommendationListAPIView, FaqListCreate, ProductDetailView, AddToCart, PlaceOrder
from .views import BannerListAPIView
from .views import CategorylistAPIView, ProductListAPIView, AboutAshyoAPIView, BrandListAPIView, CommentListAPIView





urlpatterns = [
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
    
    path('product/', ProductListAPIView.as_view()),    

      
]

