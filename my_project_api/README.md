
# API CREATION
### Create a Django Project
###### ---> django admin startproject my_project_api
### Create a Django App
###### ---> python manage.py startapp products_listing
### In my_project_api/settings.py file
###### ---> INSTALLED_APPS = [..., 'rest_framework', 'products_listing', ...]
### In 'products_listing/models.py file
###### ---> from django.db import models
###### ---> # Create your models here.
###### ---> class Product(models.Model):
###### --->     ###### ---> product_name = models.CharField(max_length = 100)
###### --->     ###### ---> product_company = models.CharField(max_length = 100)
###### --->     ###### ---> product_description = models.TextField()
###### --->     ###### ---> product_price = models.DecimalField(max_digits = 10, decimal_places = 2)
###### --->     ###### ---> product_present = models.BooleanField(default = True)
###### --->     ###### ---> def __str__(self):
###### --->     ###### --->     ###### ---> return self.name
### Run migrations to create the database tables
###### ---> python manage.py makemigrations
###### ---> python manage.py migrate
### In 'products_listing/serializers.py' file
###### ---> from rest_framework import serializers
###### ---> from products_listing.models import Product
###### ---> class ProductSerializer(serializers.ModelSerializer):
###### --->     ###### ---> class Meta:
###### --->     ###### --->     ###### ---> model = Product
###### --->     ###### --->     ###### ---> fields = "__all__"
### In 'products_listing/views.py' file
###### ---> from django.shortcuts import render
###### ---> from rest_framework import viewsets, generics
###### ---> from products_listing.models import Product
###### ---> from products_listing.serializers import ProductSerializer
###### ---> # Create your views here.
###### ---> class ProductViewSetList(generics.ListCreateAPIView):
###### --->     ###### ---> queryset = Product.objects.all()
###### --->     ###### ---> serializer_class = ProductSerializer
###### ---> class ProductViewSetDetail(generics.RetrieveUpdateDestroyAPIView):
###### --->     ###### ---> queryset = Product.objects.all()
###### --->     ###### ---> serializer_class = ProductSerializer
### In 'products_listing/urls.py' file
###### ---> from django.urls import path
###### ---> from products_listing.views import ProductViewSetDetail, ProductViewSetList

###### ---> urlpatterns = [
###### --->     ###### ---> path('products/',ProductViewSetList.as_view()),
###### --->     ###### ---> path('products/<int:pk>/', ProductViewSetDetail.as_view())
###### ---> ]
### In 'my_project_api/urls.py' file
###### ---> from django.contrib import admin
###### ---> from django.urls import path,include
###### ---> 
###### ---> urlpatterns = [
###### --->    ###### --->  path('admin/', admin.site.urls),
###### --->    ###### --->  path('api/', include('products_listing.urls'))
###### ---> ]
### Start the development server and test the api by visiting 
###### ---> 'https://localhost:8000/api/products/'
###### ---> python manage.py runserver
