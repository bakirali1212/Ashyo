from django.urls import path
from .views import CategorylistAPIView, ProductListAPIView, AboutAshyoAPIView, BrandListAPIView, CommentListAPIView





urlpatterns = [
    path('category/', CategorylistAPIView.as_view()),    
    path('about-ashyo/', AboutAshyoAPIView.as_view()),
    path('brand-list/', BrandListAPIView.as_view()),
    path('comment-list/', CommentListAPIView.as_view()),
    path('product/', ProductListAPIView.as_view()),    

      
]

