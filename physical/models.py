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
        bmi_calc = self.weight/self.height**2
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
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    activity_level = models.CharField(choices=activity_level, default='', max_length=200)
    bmr = models.FloatField(default=0)
    TDEE = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    
    def bmr_calc(self):
        bmr = 655 + ( 4.35*self.weight*2.205 )+( 4.7*self.height*2.54 ) - ( 4.7*self.age )
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
        TDEE = self.bmr_calc()*activity
        return TDEE
        
    
    def save(self, *args, **kwargs):
        self.bmr = self.bmr_calc()
        self.TDEE = self.TDEE_calc()
        super(Macro, self).save(*args, **kwargs)    
        