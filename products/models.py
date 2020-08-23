# Import libraries
from django.db import models

# Create product categories
CATEGORY = (
    ('Weights', 'Weights'),
    ('Benches', 'Benches'),
    ('Accessories', 'Accessories'),
    ('Supplements', 'Supplements'),
    ('Vitamins', 'Vitamins'),)

# Create product model
class Product(models.Model):
    
    name = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=30, choices=CATEGORY, default='Weights')
    short_description = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name