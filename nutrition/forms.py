from django import forms
from .models import Physical


class bmi(forms.ModelForm):

    class Meta:
        model = Physical
        fields = ('height','weight')