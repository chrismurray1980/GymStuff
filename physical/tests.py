from django.test import TestCase
from .models import User, Physical, Macro
from django.test import Client

setup_test_environment()

c=Client()

# BMI Tests.
class BMITests(TestCase):
    
    # Get bmi result view
    def test_bmi_result_view(self):
        """Height correctly retrieved by user"""
        response = c.get('/bmi_result/')
        self.assertEqual(response.status_code, 200)
    
    # Test setup by creating new BMI models
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
        height1 = Physical.objects.get(user=1)
        height2 = Physical.objects.get(user=2)
        self.assertEqual(height1.height, 160.00)
        self.assertEqual(height2.height, 80.00)
        
    # Get weight from user id
    def test_get_weight_from_user(self):
        """Weight correctly retrieved by user"""
        weight1 = Physical.objects.get(user=1)
        weight2 = Physical.objects.get(user=2)
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
            age=40.00,
            unit_type = 'Metric',
            activity_level = 'little exercise',
            aim ='lose weight'
            )
        Macro.objects.create(
            user= user2,
            height = 80.00,
            weight = 200.00,
            age=24.00,
            unit_type = 'Imperial',
            activity_level = 'heavy exercise',
            aim ='maintain'
            )
    
    # Get height from user id
    def test_get_height_from_user(self):
        """Height correctly retrieved by user"""
        height1 = Macro.objects.get(user=1)
        height2 = Macro.objects.get(user=2)
        self.assertEqual(height1.height, 160.00)
        self.assertEqual(height2.height, 80.00)
        
    # Get weight from user id
    def test_get_weight_from_user(self):
        """Weight correctly retrieved by user"""
        weight1 = Macro.objects.get(user=1)
        weight2 = Macro.objects.get(user=2)
        self.assertEqual(weight1.weight, 80.00)
        self.assertEqual(weight2.weight, 200.00)
        
    # Calculate user unit height:
    def test_calculate_unit_height(self):
        """Unit height calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.calculate_unit_height(), 1.60)
        self.assertEqual(imperial.calculate_unit_height(), 2.032)

    # Calculate user unit weight:
    def test_calculate_unit_weight(self):
        """Unit weight calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.calculate_unit_weight(), 80.00)
        self.assertEqual(imperial.calculate_unit_weight(), 91.00)
    
    # Calculate user bmr:
    def test_calculate_bmr(self):
        """BMR calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.bmr_calc(), 1530.40)
        self.assertEqual(imperial.bmr_calc(), 1791.05)
    
    # Calculate user TDEE:
    def test_calculate_TDEE(self):
        """TDEE calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.TDEE_calc(), 1836.48)
        self.assertEqual(imperial.TDEE_calc(), 3089.56)
    
    # Calculate user daily calorie goal:
    def test_calculate_daily_calorie_goal(self):
        """Calorie goal calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.calculated_calorie_goal(), 1561.01)
        self.assertEqual(imperial.calculated_calorie_goal(), 3089.56)
    
    # Calculate user daily carb weight:
    def test_calculate_daily_carb_weight(self):
        """Carb weight calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.carb_calc(), 117.00)
        self.assertEqual(imperial.carb_calc(), 309.00)

    # Calculate user daily protein weight:
    def test_calculate_daily_protein_weight(self):
        """Protein weight calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.protein_calc(), 156.00)
        self.assertEqual(imperial.protein_calc(), 232.00)        

    # Calculate user daily fat weight:
    def test_calculate_daily_fat_weight(self):
        """Fat weight calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.fat_calc(), 52.00)
        self.assertEqual(imperial.fat_calc(), 103.00)  

    # Calculate user daily carb percent:
    def test_calculate_daily_carb_percent(self):
        """Carb percent calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.carb_percent_calc()*100, 30.00)
        self.assertEqual(imperial.carb_percent_calc()*100, 40.00)

    # Calculate user daily protein weight:
    def test_calculate_daily_protein_percent(self):
        """Protein percent calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.protein_percent_calc()*100, 40.00)
        self.assertEqual(imperial.protein_percent_calc()*100, 30.00)        

    # Calculate user daily fat percent:
    def test_calculate_daily_fat_percent(self):
        """Fat weight calculated correctly"""
        metric = Macro.objects.get(unit_type="Metric")
        imperial = Macro.objects.get(unit_type="Imperial")
        self.assertEqual(metric.fat_percent_calc()*100, 30.00)
        self.assertEqual(imperial.fat_percent_calc()*100, 30.00)  


