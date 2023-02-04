from django.urls import path
from products_listing.views import ProductViewSetDetail, ProductViewSetList

urlpatterns = [
    path('products/',ProductViewSetList.as_view()),
    path('products/<int:pk>/', ProductViewSetDetail.as_view())
]