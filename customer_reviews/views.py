from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import customer_review
from .forms import ReviewForm
from products.models import Product
import datetime
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory

def customer_reviews(request, id):
    latest_review_list = customer_review.objects.filter(product__id=id).order_by('-date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'customer_reviews.html', context)
 
def review_detail(request, id):
    review = get_object_or_404(customer_review, pk=id)
    return render(request, 'review_detail.html', {'review': review})

'''
def create_or_edit_review(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the review ID
    is null or not
    """
    review = get_object_or_404(customer_review, pk=pk) if pk else None
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(review_detail, review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review_form.html', {'form': form})
'''
