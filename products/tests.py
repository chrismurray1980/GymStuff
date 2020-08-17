from django.test import TestCase
from .models import Product

# Product model tests.
class ProductTests(TestCase):
    
    
    # Test setup by creating new products
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


    # Test name field of product model from short description
    def test_name_from_short_description(self):
        """Name correctly identified from short_description"""
        test_name_object_1 = Product.objects.get(short_description="A weight plate")
        test_name_object_2 = Product.objects.get(short_description="A pull up bar")
        self.assertEqual(str(test_name_object_1.name), '10kg weight')
        self.assertEqual(str(test_name_object_2.name), 'pull up bar')
        
        
    # Test name field of product model from description
    def test_name_from_description(self):
        """Name correctly identified from description"""
        test_name_object_1 = Product.objects.get(description="A light weight plate")
        test_name_object_2 = Product.objects.get(description="A door mounted pull up bar")
        self.assertEqual(str(test_name_object_1.name), '10kg weight')
        self.assertEqual(str(test_name_object_2.name), 'pull up bar')
        
        
    # Test name field of product model from price
    def test_name_from_price(self):
        """Name correctly identified from price"""
        test_name_object_1 = Product.objects.get(price="50")
        test_name_object_2 = Product.objects.get(price="30")
        self.assertEqual(str(test_name_object_1.name), '10kg weight')
        self.assertEqual(str(test_name_object_2.name), 'pull up bar') 


    # Test short description field of product model from name
    def test_short_description_from_name(self):
        """Name correctly identified from short_description"""
        test_short_description_object_1 = Product.objects.get(name="10kg weight")
        test_short_description_object_2 = Product.objects.get(name="pull up bar")
        self.assertEqual(str(test_short_description_object_1.short_description), 'A weight plate')
        self.assertEqual(str(test_short_description_object_2.short_description), 'A pull up bar')
        
        
    # Test short description field of product model from description
    def test_short_description_from_description(self):
        """Name correctly identified from description"""
        test_short_description_object_1 = Product.objects.get(description="A light weight plate")
        test_short_description_object_2 = Product.objects.get(description="A door mounted pull up bar")
        self.assertEqual(str(test_short_description_object_1.short_description), 'A weight plate')
        self.assertEqual(str(test_short_description_object_2.short_description), 'A pull up bar') 
        
        
    # Test short description field of product model from price
    def test_short_description_from_price(self):
        """Name correctly identified from price"""
        test_short_description_object_1 = Product.objects.get(price="50")
        test_short_description_object_2 = Product.objects.get(price="30")
        self.assertEqual(str(test_short_description_object_1.short_description), 'A weight plate')
        self.assertEqual(str(test_short_description_object_2.short_description), 'A pull up bar')
