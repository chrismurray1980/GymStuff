#Import libraries, modesl and forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import customer_review
from .forms import ReviewForm
from products.models import Product
import datetime

# Create customer review view
def customer_reviews(request, id):
    # Get product from id
    product=get_object_or_404(Product, id=id)
    # List latest reviews by date
    latest_review_list = customer_review.objects.filter(product__id=id).order_by('-date')[:9]
    # Create view context
    context = {'latest_review_list':latest_review_list, 'product':product}
    # Render review page
    return render(request, 'customer_reviews.html', context)

