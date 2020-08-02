from django import forms
from .models import Physical, Macro


class bmi(forms.ModelForm):

    class Meta:
        model = Physical
        fields = ('height','weight')
        

class macro(forms.ModelForm):

    class Meta:
        model = Macro
        fields = ('height','weight', 'age', 'activity_level', 'aim')