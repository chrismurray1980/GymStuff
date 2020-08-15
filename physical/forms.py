from django import forms
from .models import Physical, Macro


class bmi(forms.ModelForm):

    class Meta:
        model = Physical
        fields = ('unit_type', 'height','weight')
        

class macro(forms.ModelForm):

    class Meta:
        model = Macro
        fields = ('unit_type', 'height','weight', 'age', 'activity_level', 'aim')