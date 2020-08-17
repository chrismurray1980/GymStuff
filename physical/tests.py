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

    # Calculate user unit height:
    def test_calculate_unit_height(self):
        """Unit height calculated correctly"""
        metric = Physical.objects.get(unit_type="Metric")
        imperial = Physical.objects.get(unit_type="Imperial")
        self.assertEqual(metric.calculate_unit_height(), 1.60)
        self.assertEqual(imperial.calculate_unit_height(), 2.03)

    # Calculate user unit weight:
    def test_calculate_unit_weight(self):
        """Unit weight calculated correctly"""
        metric = Physical.objects.get(unit_type="Metric")
        imperial = Physical.objects.get(unit_type="Imperial")
        self.assertEqual(metric.calculate_unit_weight(), 80.00)
        self.assertEqual(imperial.calculate_unit_weight(), 90.72)
        
    # Calculate user BMI
    def test_calculate_bmi(self):
        """Bmi correctly calculated"""
        metric = Physical.objects.get(unit_type="Metric")
        imperial = Physical.objects.get(unit_type="Imperial")
        self.assertEqual(metric.calculated_bmi(), 31.25)
        self.assertEqual(imperial.calculated_bmi(), 22.04)
        
            #unit_height = Physical.calculate_unit_height(),
            #unit_weight = calculate_unit_weight(self),
            #bmi_calc = calculated_bmi(self),
            #bmi_category = category_calc(self),