from django.test import TestCase
#Import libraries views and models
from django.test import TestCase, Client
from .models import Product, customer_review

# Customer review model tests.
class CustomerReviewTests(TestCase):
    
    # Test setup by creating new customer review models
    def setUp(self):
        #create product models 
        product1= Product.objects.create(
            name="10kg weight", 
            category="Weights", 
            short_description="A weight plate",
            description="A light weight plate",
            price ="50.00"
        )
        product2=Product.objects.create(
            name="pull up bar", 
            category="Accessories", 
            short_description="A pull up bar",
            description="A door mounted pull up bar",
            price ="30.00"
            )
        #create model objects
        customer_review.objects.create(
            product = product1,
            username = 'Jim',
            headline = 'Great',
            comment = 'Superb',
            rating = 5
        )
        customer_review.objects.create(
            product = product2,
            username = 'Bob',
            headline = 'Rubbish',
            comment = 'Poor',
            rating = 1
        )
        
     # Test username field of customer review model from product name
    def test_name_from_category(self):
        """Username correctly identified from product name"""
        test_username_object_1 = Product.objects.get(category="10kg weight")
        test_username_object_2 = Product.objects.get(category="pull up bar")
        self.assertEqual(str(test_username_object_1.username), 'Jim')
        self.assertEqual(str(test_username_object_2.username), 'Bob')
        
