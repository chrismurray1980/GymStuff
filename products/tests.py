from django.test import TestCase
from .models import Product

# Product model tests.
class ProductTests(TestCase):
    
    # Test setup by craeting new products
    def setUp(self):
        Product.objects.create(
            name="10kg weight", 
            category="Weights", 
            short_description="A weight plate",
            description="A light weight plate",
            price ="50"
            )
        Product.objects.create(
            name="pull up bar", 
            category="Accessories", 
            short_description="A pull up bar",
            description="A door mounted pull up bar",
            price ="30"
            )

    # Test name field of product model from short descirption
    def test_name_from_short_description(self):
        """Name correctly identified from short_description"""
        test_name_object_1 = Product.objects.get(short_description="A weight plate")
        test_name_object_2 = Product.objects.get(short_description="A pull up bar")
        self.assertEqual(str(test_name_object_1), '10kg weight')
        self.assertEqual(str(test_name_object_1), 'pull up bar')
