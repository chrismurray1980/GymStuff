from django.test import TestCase
from products.models import Product
from .models import customer_review

# Customer review model tests.
class CustomerReviewTests(TestCase):
    
    # Test setup by creating new customer review models
    def setUp(self):
        #create user models 
        user1 = User.objects.create(id=1, username='Bob', email='bob@example.com')
        user2 = User.objects.create(id=2, username='Jan', email='jan@example.com')
        #create model objects
        Physical.objects.create(
            user = user1,
            height = 160.00,
            weight = 80.00,
            unit_type = 'Metric'
            )
        Physical.objects.create(
            user= user2,
            height = 80.00,
            weight = 200.00,
            unit_type = 'Imperial'
            )
