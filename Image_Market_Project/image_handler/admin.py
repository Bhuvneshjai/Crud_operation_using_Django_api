from django.contrib import admin
from image_handler.models import Category, Image

# Register your models here.
admin.site.register(Category)
admin.site.register(Image)