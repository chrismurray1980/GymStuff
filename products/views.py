from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Product
from customer_reviews.forms import ReviewForm
from customer_reviews.models import customer_review
import datetime
from django.conf.urls import url

# display all products
def all_products(request):
    weights = Product.objects.filter(category='Weights')
    benches = Product.objects.filter(category='Benches')
    accessory = Product.objects.filter(category='Accessories')
    supplements = Product.objects.filter(category='Supplements')
    return render(request, "all_products.html", {"weights": weights, "benches": benches, "accessory":accessory, 'supplements': supplements})

#display product page
def product(request, id):
    product = Product.objects.get(pk=id)
    form = ReviewForm()
    return render(request, 'product.html', {'product': product, 'form':form })
    

def create_or_edit_review(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        username = form.cleaned_data['username']
        review = customer_review()
        review.product = Product.objects.get(id=product_id)
        review.username = username
        review.rating = rating
        review.comment = comment
        review.date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('product', args=(product.id,)))

    return render(request, 'product.html', {'product': product, 'form': form})

