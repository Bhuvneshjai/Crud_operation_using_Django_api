from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    product_company = models.CharField(max_length = 100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    product_present = models.BooleanField(default = True)

    def __str__(self):
        return self.name