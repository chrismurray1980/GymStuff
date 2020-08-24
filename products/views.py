# Import libraries, models and forms
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Product
from customer_reviews.forms import ReviewForm
from customer_reviews.models import customer_review
import datetime
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Display product categories
def all_products(request):
    # Get products based on category
    weights = Product.objects.filter(category='Weights').order_by('-price')[:3] 
    benches = Product.objects.filter(category='Benches').order_by('-price')[:3]
    accessory = Product.objects.filter(category='Accessories').order_by('-price')[:3]
    supplements = Product.objects.filter(category='Supplements').order_by('-price')[:3]
    vitamins = Product.objects.filter(category='Vitamins').order_by('-price')[:3]
    # Render all products view
    return render(request, "all_products.html", {"weights": weights, "benches": benches, "accessory":accessory, "supplements": supplements, "vitamins": vitamins})

# Display product page
def product(request, id):
    # Get product via id
    product = Product.objects.get(pk=id)
    # Generate review form
    form = ReviewForm()
    # Get product page
    return render(request, 'product.html', {'product': product, 'form':form })

# Create product review    
@login_required
def create_or_edit_review(request, product_id):
    # Get product by id
    product = Product.objects.get(id=product_id)
    # Create form instance 
    form = ReviewForm(request.POST)
    # Validate form
    if form.is_valid():
        # Get data from form
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        username = form.cleaned_data['username']
        headline = form.cleaned_data['headline']
        # Create model instance
        review = customer_review()
        # Add data to model instance
        review.product = Product.objects.get(id=product_id)
        review.username = username
        review.rating = rating
        review.comment = comment
        review.headline = headline
        review.date = datetime.datetime.now()
        review.save()
        # Inform user that review successfully submitted
        messages.success(request, "You have successfully reviewed this product")
        # Return to product view
        return HttpResponseRedirect(reverse('product', args=(product.id,)))
    # Render product view
    return render(request, 'product.html', {'product': product, 'form': form})

# Create similar products view
def view_similar_products(request, product_id):
    # Get product by id
    product = Product.objects.get(id=product_id)
    # Find product category
    product_category = product.category
    # Search db for products of category and order by price
    category = Product.objects.filter(category=product_category).order_by('price')
    # Display product category page
    return render(request, "product_category.html", {"products": category})
    
    
    
