# CRUD OPERATION USING DJANGO API (REST API)
### Here are the steps to create a Django API for performing CRUD operations:

### Create a new Django project and app using the command line:
##### ---> $ django-admin startproject project_name
---> $ cd project_name
---> $ python manage.py startapp app_name
#### Define the models in the app's models.py file using Django's ORM. For example:
---> from django.db import models

---> class Book(models.Model):
------>    title = models.CharField(max_length=200)
------>    author = models.CharField(max_length=200)
------>    published_date = models.DateField()

------>    def __str__(self):
---------        return self.title
#### Create serializers in the app's serializers.py file to convert the model instances to JSON format. For example:
---> from rest_framework import serializers
---> from .models import Book

---> class BookSerializer(serializers.ModelSerializer):
------>    class Meta:
------>        model = Book
------>        fields = ('id', 'title', 'author', 'published_date')
#### Create views in the app's views.py file to handle the CRUD operations. For example:
---> from rest_framework import generics
---> from .models import Book
---> from .serializers import BookSerializer

---> class BookListCreate(generics.ListCreateAPIView):
------>    queryset = Book.objects.all()
------>    serializer_class = BookSerializer

---> class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
------>    queryset = Book.objects.all()
------>    serializer_class = BookSerializer
#### Define the URLs for the API in the project's urls.py file. For example:
---> from django.urls import path
---> from app_name.views import BookListCreate, BookRetrieveUpdateDestroy

---> urlpatterns = [
------>    path('books/', BookListCreate.as_view(), name='book-list-create'),
------>    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
------> ]
#### Run the development server using the command line:
---> $ python manage.py runserver
#### Test the API using a tool like curl, Postman, or a web browser.
#### With these steps, you should have a basic Django API for performing CRUD operations on your database. You can customize and extend the API as needed for your application's requirements.
