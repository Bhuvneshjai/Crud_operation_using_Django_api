from django.shortcuts import render
from rest_framework import viewsets, generics
from products_listing.models import Product
from products_listing.serializers import ProductSerializer

# Create your views here.
class ProductViewSetList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewSetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer