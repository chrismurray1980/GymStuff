from django.shortcuts import render
from .models import Product

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
    return render(request, 'product.html', {'product': product })

