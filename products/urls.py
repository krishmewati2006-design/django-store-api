from django.urls import path
from .views import Product_list, Product_detail, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', Product_list.as_view(), name='product_list'),
    path('<int:pk>/', Product_detail.as_view(), name='product_detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', RegisterView.as_view(), name='register'),
] 