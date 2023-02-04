from django.urls import path
from api_app.views import ProductList, ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
]
