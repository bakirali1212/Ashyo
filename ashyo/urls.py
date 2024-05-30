from django.urls import path
from .views import KategoriyaListAPIView



urlpatterns = [
    path('kategoriya-list/', KategoriyaListAPIView.as_view()),
      
]

