from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "all_products.html", {"products": products})

def weight_search(request):
    weights = Product.objects.filter(category='Weights')
    return render(request, "all_products.html", {"products": weights})
    
def supplement_search(request):
    supplement = Product.objects.filter(category='Supplements')
    return render(request, "all_products.html", {"products": supplement})
    
def bench_search(request):
    bench = Product.objects.filter(category='Benches')
    return render(request, "all_products.html", {"products": bench})
    
def accessory_search(request):
    accessory = Product.objects.filter(category='Accessories')
    return render(request, "all_products.html", {"products": accessory})

def vitamin_search(request):
    vitamin = Product.objects.filter(category='Vitamins')
    return render(request, "all_products.html", {"products": vitamin})
    