from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import customer_review
from products.models import Product
import datetime
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

def customer_reviews(request, id):
    latest_review_list = customer_review.objects.filter(product__id=id).order_by('-date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'customer_reviews.html', context)
                
#def review_detail(request, id):
 #   review = customer_review.objects.filter(id=id)
  #  return render(request, 'review_detail.html', {'review': review})


def review_detail(request, id):
    review = get_object_or_404(customer_review, pk=id)
    return render(request, 'review_detail.html', {'review': review})

    
    
    
    
    
    