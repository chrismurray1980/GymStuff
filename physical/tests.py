from django.test import TestCase
from .models import User, Physical, Macro

# BMI model tests.
class BMITests(TestCase):
    
    # Test setup by creating new bmi model
    def setUp(self):
        user1 = User.objects.create(id=1, username='Bob', email='bigbadbob@notgotajob')
        user2 = User.objects.create(id=2, username='Jill', email='sillylittlejilly@notgotawilly')
        Physical.objects.create(
            user =user1,
            height = 160,
            weight = 80,
            unit_type = 'Metric'
            )
        Physical.objects.create(
            user=user2,
            height = 80,
            weight = 200,
            unit_type = 'Imperial'
            )

    
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