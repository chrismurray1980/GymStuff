from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Product
from customer_reviews.forms import ReviewForm
from customer_reviews.models import customer_review
import datetime
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

# display all products
def all_products(request):
    weights = Product.objects.filter(category='Weights').order_by('-price')[:3] 
    benches = Product.objects.filter(category='Benches').order_by('-price')[:3]
    accessory = Product.objects.filter(category='Accessories').order_by('-price')[:3]
    supplements = Product.objects.filter(category='Supplements').order_by('-price')[:3]
    vitamins = Product.objects.filter(category='Vitamins').order_by('-price')[:3]
    return render(request, "all_products.html", {"weights": weights, "benches": benches, "accessory":accessory, "supplements": supplements, "vitamins": vitamins})

#display product page
def product(request, id):
    product = Product.objects.get(pk=id)
    form = ReviewForm()
    return render(request, 'product.html', {'product': product, 'form':form })
    
@login_required
def create_or_edit_review(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        username = form.cleaned_data['username']
        headline = form.cleaned_data['headline']
        review = customer_review()
        review.product = Product.objects.get(id=product_id)
        review.username = username
        review.rating = rating
        review.comment = comment
        review.headline = headline
        review.date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('product', args=(product.id,)))

    return render(request, 'product.html', {'product': product, 'form': form})

