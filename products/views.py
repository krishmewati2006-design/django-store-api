from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
'''

'''

class RegisterView(APIView):
    permission_classes = []
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if username is None or password is None:
            return Response({'Message': "Missing Required Fields"}, status=400)
        
        try:
            user = User.objects.create_user(username=username, password=password)
            token = Token.objects.create(user=user)
        except IntegrityError:
            return Response({"Error": "Username Already Exists."}, status=400)
        
        return Response({'Token': token.key}, status=201)

class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username = request.data.get('username'),
            password = request.data.get('password')
        )
        if user:
            token,_= Token.objects.get_or_create(user=user)
            return Response({'Token': token.key})
        return Response({'Error': 'Invalid Credentials'}, status=400)

class Product_list(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         

class Product_detail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product)

            return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        
        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
