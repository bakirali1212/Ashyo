from django.urls import path
from . import views
from .views import  ProductListAPIView, AboutAshyoAPIView, BrandListAPIView, CommentListAPIView
from .views import RecommendationListAPIView, FaqListCreate, ProductDetailView, AddToCart, PlaceOrder, MostpopularproductListAPIView
from .views import BannerListAPIView
from .views import CategorylistAPIView,  FlialLocationListAPIView





urlpatterns = [
    path('product-filter/', views.ProductListFIlter.as_view() ),
    path('category/', CategorylistAPIView.as_view()),    
    path('about-ashyo/', AboutAshyoAPIView.as_view()),
    path('brand-list/', BrandListAPIView.as_view()),
    path('comment-list/', CommentListAPIView.as_view()),
    path('banner-list/', BannerListAPIView.as_view()),
    path('recommendation-list/', RecommendationListAPIView.as_view()),
    path('faqs/', FaqListCreate.as_view()),
    path('product-detail/<int:pk>/', ProductDetailView.as_view()),
    path('add-to-cart/<int:pk>/', AddToCart.as_view()),
    path('place-order/', PlaceOrder.as_view()),
    path('mostpopular-productslist/', MostpopularproductListAPIView.as_view()),   
    path('product/', ProductListAPIView.as_view()),    
    path('send-aplicationns/', views.SendAplicationCreateAPIView.as_view()),
    path('Cridet-send-image/', views.CreditImageCreateAPIView.as_view() ),
    
    path('Flial-list/', FlialLocationListAPIView.as_view()), 
    path('client-date/', views.ClientdataCreatAPIView.as_view()),   

      
]

