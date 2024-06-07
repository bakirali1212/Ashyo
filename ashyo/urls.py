from django.urls import path
from . import views


urlpatterns = [
    path('product-filter-price/', views.ProductListFIlterPrice.as_view() ),
    path('category/', views.CategorylistAPIView.as_view()),    
    path('about-ashyo/', views.AboutAshyoAPIView.as_view()),
    path('brand-list/', views.BrandListAPIView.as_view()),
    path('comment-list/', views.CommentListAPIView.as_view()),
    path('banner-list/', views.BannerListAPIView.as_view()),
    path('recommendation-list/', views.RecommendationListAPIView.as_view()),
    path('faqs/', views.FaqListCreate.as_view()),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view()),
    path('add-to-cart/<int:pk>/', views.AddToCart.as_view()),
    path('place-order/', views.PlaceOrder.as_view()),
    path('mostpopular-productslist/', views.MostpopularproductListAPIView.as_view()),   
    path('product/', views.ProductListAPIView.as_view()),    
    path('send-aplicationns/', views.SendAplicationCreateAPIView.as_view()),
    path('Cridet-send-image/', views.CreditImageCreateAPIView.as_view() ),\
    path('user-register/', views.UserRegister.as_view() ),
    path('verify/', views.VerifyAPIView.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('client-date/', views.ClientdataCreatAPIView.as_view()),   

      
]

