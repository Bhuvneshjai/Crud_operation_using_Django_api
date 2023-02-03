# API CREATION OF PRODUCT 
## Create a Django Project
# ---> django-admin startproject my_project_api
## Create a Django App
# ---> python manage.py startapp product_listing
## In the 'my_project_api/settings.py' file
# ---> INSTALLED_APPS = [... 'product_listing', ...]
## In the 'product_listing/models.py' file
# ---> from django.db import models
# ---> class Product(models.Model):
    # ---> # ---> product_name = models.CharField(max_length = 100)
    # ---> # ---> product_company = models.CharField(max_length = 100)
    # ---> # ---> product_description = models.TextField()
    # ---> # ---> product_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    # ---> # ---> product_present = models.BooleanField(default = True)

    # ---> # ---> def __str__(self):
        # ---> # ---> return self.name
