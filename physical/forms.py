# Import libraries and models
from django import forms
from .models import Physical, Macro

# Create bmi form
class bmi(forms.ModelForm):

    class Meta:
        model = Physical
        fields = ('unit_type', 'height','weight')
        
# Create model form
class macro(forms.ModelForm):

    class Meta:
        model = Macro
        fields = ('unit_type', 'height','weight', 'age', 'activity_level', 'aim')