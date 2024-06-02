from django.urls import path
from .views import CategoryListAPIView, ProductListAPIView, AboutAshyoAPIView, BrandListAPIView, CommentListAPIView



urlpatterns = [
    path('category-list/', CategoryListAPIView.as_view()),
    path('product-list/', ProductListAPIView.as_view()),
    path('about-ashyo/', AboutAshyoAPIView.as_view()),
    path('brand-list/', BrandListAPIView.as_view()),
    path('comment-list/', CommentListAPIView.as_view()),
      
]

