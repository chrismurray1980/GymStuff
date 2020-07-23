from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import customer_review
from products.models import Product
import datetime

def customer_reviews(request):
    latest_review_list = customer_review.objects.order_by('-date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'customer_reviews.html', context)


def review_detail(request, customer_review_id):
    review = get_object_or_404(customer_review, pk=customer_review_id)
    return render(request, 'review_detail.html', {'review': review})