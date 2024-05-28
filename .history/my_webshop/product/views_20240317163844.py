from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from.serializers import ProductSerializer

class LatestProductsListView(APIView):
    def get(self,request, form=None):
        products = Product.objects.all() [0:4]
        serializer = ProductSerializer(products, many = True)   