from django.shortcuts import render
from .models import Product

# display all products
def all_products(request):
    products = Product.objects.all()
    return render(request, "all_products.html", {"products": products})

#display product page
def product(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product.html', {'product': product })
