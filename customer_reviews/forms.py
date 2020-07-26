from django import forms
from .models import customer_review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = customer_review
        fields = ('username', 'comment', 'rating')
