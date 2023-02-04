from django. contrib import admin
from django.urls import path, include
from products_listing.views import ProductViewSetDetail, ProductViewSetList
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'products',ProductViewSetList.as_view())
# router.register(r'products/<int:pk>/', ProductViewSetDetail.as_view())

urlpatterns = [
    # path('',include(router.urls))
    path('products/',ProductViewSetList.as_view()),
    path('products/<int:pk>/', ProductViewSetDetail.as_view())
]