from django.urls import path
from .views import ClientListAPIView



urlpatterns = [
    path('client-list/', ClientListAPIView.as_view()),
      
]

