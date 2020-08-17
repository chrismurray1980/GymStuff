from django.test import TestCase
from .models import User, Physical, Macro

# BMI model tests.
class BMITests(TestCase):
    
    # Test setup by creating new bmi models
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

    # Get height from user id
    def test_get_height_from_user(self):
        """Height correctly retrieved by user"""
        height1 = Physical.objects.get(user='user1')
        height2 = Physical.objects.get(user='user2')
        self.assertEqual(height1.height, 160.00)
        self.assertEqual(height2.height, 80.00)
        
    # Get weight from user id
    def test_get_weight_from_user(self):
        """Weight correctly retrieved by user"""
        weight1 = Physical.objects.get(user='user1')
        weight2 = Physical.objects.get(user='user2')
        self.assertEqual(weight1.weight, 80.00)
        self.assertEqual(weight2.weight, 200.00)
        
    # Calculate user unit height:
    def test_calculate_unit_height(self):
        """Unit height calculated correctly"""
        metric = Physical.objects.get(unit_type="Metric")
        imperial = Physical.objects.get(unit_type="Imperial")
        self.assertEqual(metric.calculate_unit_height(), 1.60)
        self.assertEqual(imperial.calculate_unit_height(), 2.032)

    # Calculate user unit weight:
    def test_calculate_unit_weight(self):
        """Unit weight calculated correctly"""
        metric = Physical.objects.get(unit_type="Metric")
        imperial = Physical.objects.get(unit_type="Imperial")
        self.assertEqual(metric.calculate_unit_weight(), 80.00)
        self.assertEqual(imperial.calculate_unit_weight(), 91.00)
        
    # Calculate user BMI
    def test_calculate_bmi(self):
        """Bmi correctly calculated"""
        metric = Physical.objects.get(unit_type="Metric")
        imperial = Physical.objects.get(unit_type="Imperial")
        self.assertEqual(metric.calculated_bmi(), 31.25)
        self.assertEqual(imperial.calculated_bmi(), 22.04)
        
    # Calculate user BMI category
    def test_calculate_bmi_category(self):
        """Bmi category correctly calculated"""
        metric = Physical.objects.get(unit_type="Metric")
        imperial = Physical.objects.get(unit_type="Imperial")
        self.assertEqual(metric.category_calc(), 'Obese')
        self.assertEqual(imperial.category_calc(), 'Healthy')
        
        
# Macro model tests.
class MacroTests(TestCase):
    
    # Test setup by creating new bmi models
    def setUp(self):
        #create user models 
        user1 = User.objects.create(id=1, username='Bob', email='bob@example.com')
        user2 = User.objects.create(id=2, username='Jan', email='jan@example.com')
        #create model objects
        Macro.objects.create(
            user = user1,
            height = 160.00,
            weight = 80.00,
            unit_type = 'Metric'
            )
        Macro.objects.create(
            user= user2,
            height = 80.00,
            weight = 200.00,
            unit_type = 'Imperial'
            )

