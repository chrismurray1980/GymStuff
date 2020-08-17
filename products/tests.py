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
            price ="50.00"
            )
        Product.objects.create(
            name="pull up bar", 
            category="Accessories", 
            short_description="A pull up bar",
            description="A door mounted pull up bar",
            price ="30.00"
            )


    ###### NAME TESTING ######
    
    # Test name field of product model from category
    def test_name_from_category(self):
        """Name correctly identified from category"""
        test_name_object_1 = Product.objects.get(category="Weights")
        test_name_object_2 = Product.objects.get(category="Accessories")
        self.assertEqual(str(test_name_object_1.name), '10kg weight')
        self.assertEqual(str(test_name_object_2.name), 'pull up bar')

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
        test_name_object_1 = Product.objects.get(price="50.00")
        test_name_object_2 = Product.objects.get(price="30.00")
        self.assertEqual(str(test_name_object_1.name), '10kg weight')
        self.assertEqual(str(test_name_object_2.name), 'pull up bar') 


    ###### CATEGORY TESTING ######
    
        # Test category field of product model from name
    def test_category_from_name(self):
        """Category correctly identified from name"""
        test_category_object_1 = Product.objects.get(name="10kg weight")
        test_category_object_2 = Product.objects.get(name="pull up bar")
        self.assertEqual(str(test_category_object_1.category), 'Weights')
        self.assertEqual(str(test_category_object_2.category), 'Accessories')

    # Test category field of product model from short description
    def test_category_from_short_description(self):
        """Correctly identified from short_description"""
        test_category_object_1 = Product.objects.get(short_description="A weight plate")
        test_category_object_2 = Product.objects.get(short_description="A pull up bar")
        self.assertEqual(str(test_category_object_1.category), 'Weights')
        self.assertEqual(str(test_category_object_2.category), 'Accessories')
        
    # Test category field of product model from description
    def test_category_from_description(self):
        """Category correctly identified from description"""
        test_category_object_1 = Product.objects.get(description="A light weight plate")
        test_category_object_2 = Product.objects.get(description="A door mounted pull up bar")
        self.assertEqual(str(test_category_object_1.category), 'Weights')
        self.assertEqual(str(test_category_object_2.category), 'Accessories')
        
    # Test category field of product model from price
    def test_category_from_price(self):
        """Category correctly identified from price"""
        test_category_object_1 = Product.objects.get(price="50.00")
        test_category_object_2 = Product.objects.get(price="30.00")
        self.assertEqual(str(test_category_object_1.category), 'Weights')
        self.assertEqual(str(test_category_object_2.category), 'Accessories') 
    
    
    ###### SHORT DESCRIPTION TESTING ######
    
    # Test short description field of product model from name
    def test_short_description_from_name(self):
        """Short_description correctly identified from name"""
        test_short_description_object_1 = Product.objects.get(name="10kg weight")
        test_short_description_object_2 = Product.objects.get(name="pull up bar")
        self.assertEqual(str(test_short_description_object_1.short_description), 'A weight plate')
        self.assertEqual(str(test_short_description_object_2.short_description), 'A pull up bar')

    # Test short description field of product model from category
    def test_short_description_from_category(self):
        """Short_description correctly identified from category"""
        test_short_description_object_1 = Product.objects.get(category="Weights")
        test_short_description_object_2 = Product.objects.get(category="Accessories")
        self.assertEqual(str(test_short_description_object_1.short_description), 'A weight plate')
        self.assertEqual(str(test_short_description_object_2.short_description), 'A pull up bar')        
        
    # Test short description field of product model from description
    def test_short_description_from_description(self):
        """Short_description correctly identified from description"""
        test_short_description_object_1 = Product.objects.get(description="A light weight plate")
        test_short_description_object_2 = Product.objects.get(description="A door mounted pull up bar")
        self.assertEqual(str(test_short_description_object_1.short_description), 'A weight plate')
        self.assertEqual(str(test_short_description_object_2.short_description), 'A pull up bar') 
        
    # Test short description field of product model from price
    def test_short_description_from_price(self):
        """Short_description correctly identified from price"""
        test_short_description_object_1 = Product.objects.get(price="50.00")
        test_short_description_object_2 = Product.objects.get(price="30.00")
        self.assertEqual(str(test_short_description_object_1.short_description), 'A weight plate')
        self.assertEqual(str(test_short_description_object_2.short_description), 'A pull up bar')


    ###### DESCRIPTION TESTING ######
        
    # Test description field of product model from name
    def test_description_from_name(self):
        """Description correctly identified from name"""
        test_description_object_1 = Product.objects.get(name="10kg weight")
        test_description_object_2 = Product.objects.get(name="pull up bar")
        self.assertEqual(str(test_description_object_1.description), 'A light weight plate')
        self.assertEqual(str(test_description_object_2.description), 'A door mounted pull up bar')

    # Test description field of product model from category
    def test_description_from_category(self):
        """Description correctly identified from category"""
        test_description_object_1 = Product.objects.get(category="Weights")
        test_description_object_2 = Product.objects.get(category="Accessories")
        self.assertEqual(str(test_description_object_1.description), 'A light weight plate')
        self.assertEqual(str(test_description_object_2.description), 'A door mounted pull up bar')        
        
    # Test description field of product model from short description
    def test_description_from_short_description(self):
        """Description correctly identified from short description"""
        test_description_object_1 = Product.objects.get(short_description="A weight plate")
        test_description_object_2 = Product.objects.get(short_description="A pull up bar")
        self.assertEqual(str(test_description_object_1.description), 'A light weight plate')
        self.assertEqual(str(test_description_object_2.description), 'A door mounted pull up bar') 
        
        
    # Test description field of product model from price
    def test_description_from_price(self):
        """Description correctly identified from price"""
        test_description_object_1 = Product.objects.get(price="50.00")
        test_description_object_2 = Product.objects.get(price="30.00")
        self.assertEqual(str(test_description_object_1.description), 'A light weight plate')
        self.assertEqual(str(test_description_object_2.description), 'A door mounted pull up bar')
    
    
    ###### PRICE TESTING ######
        
    # Test price field of product model from name
    def test_price_from_name(self):
        """Price correctly identified from name"""
        test_price_object_1 = Product.objects.get(name="10kg weight")
        test_price_object_2 = Product.objects.get(name="pull up bar")
        self.assertEqual(str(test_price_object_1.price), '50.00')
        self.assertEqual(str(test_price_object_2.price), '30.00')

    # Test price field of product model from category
    def test_price_from_category(self):
        """Price correctly identified from category"""
        test_price_object_1 = Product.objects.get(category="Weights")
        test_price_object_2 = Product.objects.get(category="Accessories")
        self.assertEqual(str(test_price_object_1.price), '50.00')
        self.assertEqual(str(test_price_object_2.price), '30.00')        
        
    # Test price field of product model from short description
    def test_price_from_short_description(self):
        """Price correctly identified from short description"""
        test_price_object_1 = Product.objects.get(short_description="A weight plate")
        test_price_object_2 = Product.objects.get(short_description="A pull up bar")
        self.assertEqual(str(test_price_object_1.price), '50.00')
        self.assertEqual(str(test_price_object_2.price), '30.00') 
        
        
    # Test price field of product model from description
    def test_price_from_description_(self):
        """Price correctly identified from description"""
        test_price_object_1 = Product.objects.get(description='A light weight plate')
        test_price_object_2 = Product.objects.get(description='A door mounted pull up bar')
        self.assertEqual(str(test_price_object_1.price), '50.00')
        self.assertEqual(str(test_price_object_2.price), '30.00')
    