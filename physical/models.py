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
        ('light exercise','light exercise'),
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
    
    def save(self, *args, **kwargs):
        self.bmr = self.bmr_calc()
        self.TDEE = self.TDEE_calc()
        self.daily_calorie_goal = self.calculated_calorie_goal()
        super(Macro, self).save(*args, **kwargs)    
        