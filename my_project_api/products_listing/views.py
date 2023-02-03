from django.shortcuts import render
from rest_framework import viewsets
from products_listing.models import Product
from products_listing.serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer