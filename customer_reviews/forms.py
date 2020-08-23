# Import libraries and models
from django import forms
from .models import customer_review

# Create review form
class ReviewForm(forms.ModelForm):

    class Meta:
        model = customer_review
        fields = ('headline','username', 'comment', 'rating')
