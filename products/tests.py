from django.test import TestCase
from .models import Product

# Product model tests.
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = Product(name='Gymstuff product')
        self.assertEqual(str(test_name), 'Gymstuff product')