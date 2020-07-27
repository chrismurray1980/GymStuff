from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import customer_review
from .forms import ReviewForm
from products.models import Product
import datetime


def customer_reviews(request, id):
    product=get_object_or_404(Product, id=id)
    latest_review_list = customer_review.objects.filter(product__id=id).order_by('-date')[:9]
    context = {'latest_review_list':latest_review_list, 'product':product}
    return render(request, 'customer_reviews.html', context)

