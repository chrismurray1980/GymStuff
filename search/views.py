# Import libraries
from django.shortcuts import render
from products.models import Product
from django.db.models import Q

# Search products by word or category
def do_search(request):
    products = Product.objects.filter(Q(name__icontains=request.GET['q']) |  Q(category__icontains=request.GET['q'])).order_by('price')
    return render(request, "product_category.html", {"products": products})

# Search products by weight category
def weight_search(request):
    weights = Product.objects.filter(category='Weights').order_by('price')
    return render(request, "product_category.html", {"products": weights})

# Search products by supplement category    
def supplement_search(request):
    supplement = Product.objects.filter(category='Supplements').order_by('price')
    return render(request, "product_category.html", {"products": supplement})

# Search products by bench category    
def bench_search(request):
    bench = Product.objects.filter(category='Benches').order_by('price')
    return render(request, "product_category.html", {"products": bench})

# Search products by accessory category    
def accessory_search(request):
    accessory = Product.objects.filter(category='Accessories').order_by('price')
    return render(request, "product_category.html", {"products": accessory})

# Search products by vitamin category
def vitamin_search(request):
    vitamin = Product.objects.filter(category='Vitamins').order_by('price')
    return render(request, "product_category.html", {"products": vitamin})
    