from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime
from django.utils import timezone

# Create your models here.
class Physical(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    bmi_calc = models.FloatField(default=0)
    bmi_category = models.CharField(default='', max_length=200)
    date_now = models.DateTimeField(auto_now_add=True)
    
    def calculated_bmi(self):
        bmi_calc = round( self.weight/self.height**2, 2)
        return bmi_calc
        
    def category_calc(self):
        bmi_calc=self.calculated_bmi()
        if (bmi_calc < 18.5):
            bmi_category='Underweight'
        elif (bmi_calc >= 18.5) and (bmi_calc < 25):
            bmi_category='Healthy'
        elif (bmi_calc >= 25) and (bmi_calc < 30):
            bmi_category='Overweight'
        elif (bmi_calc >= 30) and (bmi_calc < 35):
            bmi_category='Obese'   
        elif (bmi_calc >= 35) and (bmi_calc < 40):
            bmi_category='Severely obese'    
        elif (bmi_calc >= 40) and (bmi_calc < 50):
            bmi_category='Morbidly obese'
        elif (bmi_calc >= 50):
            bmi_category='Super obese'
        else:
            bmi_category='No data available'
        return bmi_category
        
    def save(self, *args, **kwargs):
        self.bmi_calc = self.calculated_bmi()
        self.bmi_category = self.category_calc()
        super(Physical, self).save(*args, **kwargs)    
        

class Macro(models.Model):
    
    activity_level = (
        ('little exercise', 'little exercise'),
        ('moderate exercise', 'moderate exercise'),
        ('heavy exercise', 'heavy exercise'),
    )
    
    aim = (
        ('lose weight', 'lose weight'),
        ('maintain', 'maintain'),
        ('gain muscle', 'gain muscle'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    activity_level = models.CharField(choices=activity_level, default='', max_length=200)
    bmr = models.FloatField(default=0)
    TDEE = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    aim = models.CharField(choices=aim, default='', max_length=200)
    daily_calorie_goal = models.FloatField(default=0)
    carb_weight = models.FloatField(default=0)
    protein_weight = models.FloatField(default=0)
    fat_weight = models.FloatField(default=0)
    carb_percent = models.FloatField(default=0)
    protein_percent = models.FloatField(default=0)
    fat_percent = models.FloatField(default=0)
    
    def bmr_calc(self):
        bmr = round( 655 + ( 4.35*self.weight*2.205 )+( 4.7*self.height*39.37 ) - ( 4.7*self.age ), 2)
        return bmr
        
    def TDEE_calc(self):
        activity=0
        if self.activity_level =='little exercise':
            activity=1.2
        elif self.activity_level =='light exercise':
            activity=1.375
        elif self.activity_level =='moderate exercise':
            activity=1.55
        elif self.activity_level =='heavy exercise':
            activity=1.725
        TDEE = round( self.bmr_calc()*activity, 2)
        return TDEE
    
    def calculated_calorie_goal(self):
        adjustment=0
        if self.aim =='lose weight':
            adjustment=0.85
        elif self.aim =='maintain':
            adjustment=1
        elif self.aim =='gain muscle':
            adjustment=1.15
        daily_calorie_goal = round( self.TDEE_calc()*adjustment, 2)
        return daily_calorie_goal    
    
    def carb_calc(self):
        carb_ratio = 0
        if self.aim =='lose weight':
            carb_ratio = 0.3
        elif self.aim =='maintain':
            carb_ratio=0.4
        elif self.aim =='gain muscle':
            carb_ratio=0.5
        carb_ratio = self.calculated_calorie_goal()*carb_ratio
        carb_weight_per_gram = 4
        carb_weight = round( carb_ratio/carb_weight_per_gram , 0)
        return carb_weight
    
    def protein_calc(self):
        protein_ratio = 0
        if self.aim =='lose weight':
            protein_ratio = 0.4
        elif self.aim =='maintain':
            protein_ratio=0.3
        elif self.aim =='gain muscle':
            protein_ratio=0.3
        protein_ratio = self.calculated_calorie_goal()*protein_ratio
        protein_weight_per_gram = 4
        protein_weight = round( protein_ratio/protein_weight_per_gram , 0)
        return protein_weight
        
    def fat_calc(self):
        fat_ratio = 0
        if self.aim =='lose weight':
            fat_ratio = 0.3
        elif self.aim =='maintain':
            fat_ratio=0.3
        elif self.aim =='gain muscle':
            fat_ratio=0.2
        fat_ratio = self.calculated_calorie_goal()*fat_ratio
        fat_weight_per_gram = 9
        fat_weight = round( fat_ratio/fat_weight_per_gram , 0)
        return fat_weight
    
    def carb_percent_calc(self):
        carb_percent= 0
        if self.aim =='lose weight':
            carb_percent = 0.3
        elif self.aim =='maintain':
            carb_percent=0.4
        elif self.aim =='gain muscle':
            carb_percent=0.5
        return carb_percent
        
    def protein_percent_calc(self):
        protein_percent = 0
        if self.aim =='lose weight':
            protein_percent = 0.4
        elif self.aim =='maintain':
            protein_percent=0.3
        elif self.aim =='gain muscle':
            protein_percent=0.3
        return protein_percent

    def fat_percent_calc(self):
        fat_percent = 0
        if self.aim =='lose weight':
            fat_percent = 0.3
        elif self.aim =='maintain':
            fat_percent=0.3
        elif self.aim =='gain muscle':
            fat_percent=0.2
        return fat_percent
        
    def save(self, *args, **kwargs):
        self.bmr = self.bmr_calc()
        self.TDEE = self.TDEE_calc()
        self.daily_calorie_goal = self.calculated_calorie_goal()
        self.carb_weight = self.carb_calc()
        self.protein_weight = self.protein_calc()
        self.fat_weight = self.fat_calc()
        self.carb_percent = self.carb_percent_calc()
        self.protein_percent = self.protein_percent_calc()
        self.fat_percent = self.fat_percent_calc()
        super(Macro, self).save(*args, **kwargs)    
        
        
        