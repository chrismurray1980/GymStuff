#Import libraries views and models
from django.test import TestCase, Client
from .models import Product, customer_review

from django.shortcuts import render, get_object_or_404, redirect, reverse

# Customer review model tests.
class CustomerReviewTests(TestCase):
    
    # Test setup by creating new customer review models
    def setUp(self):
        #create product models 
        product1= Product.objects.create(
            id=1,
            name="10kg weight", 
            category="Weights", 
            short_description="A weight plate",
            description="A light weight plate",
            price ="50.00"
        )
        product2=Product.objects.create(
            id=2,
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
        
    # Test username field of customer review model from product 
    def test_name_from_product(self):
        """Username correctly identified from product """
        test_username_object_1 = customer_review.objects.get(product=1)
        test_username_object_2 = customer_review.objects.get(product=2)
        self.assertEqual(str(test_username_object_1.username), 'Jim')
        self.assertEqual(str(test_username_object_2.username), 'Bob')
        
    # Test headline field of customer review model from product 
    def test_headline_from_product(self):
        """Headline correctly identified from product """
        test_headline_object_1 = customer_review.objects.get(product=1)
        test_headline_object_2 = customer_review.objects.get(product=2)
        self.assertEqual(str(test_headline_object_1.headline), 'Great')
        self.assertEqual(str(test_headline_object_2.headline), 'Rubbish')

    # Test comment field of customer review model from product 
    def test_comment_from_product(self):
        """Comment correctly identified from product """
        test_comment_object_1 = customer_review.objects.get(product=1)
        test_comment_object_2 = customer_review.objects.get(product=2)
        self.assertEqual(str(test_comment_object_1.comment), 'Superb')
        self.assertEqual(str(test_comment_object_2.comment), 'Poor')      
        
    # Test rating field of customer review model from product 
    def test_rating_from_product(self):
        """Rating correctly identified from product """
        test_rating_object_1 = customer_review.objects.get(product=1)
        test_rating_object_2 = customer_review.objects.get(product=2)
        self.assertEqual(str(test_rating_object_1.rating), '5')
        self.assertEqual(str(test_rating_object_2.rating), '1') 
        
    #Test customer review page rendered
    def test_customer_review_page(self):
        url = reverse('customer_reviews/1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_reviews.html')
