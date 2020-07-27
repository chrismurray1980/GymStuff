from django.shortcuts import render, redirect, reverse
from products.models import Product
from customer_reviews.forms import ReviewForm
from django.contrib import messages

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    if request.POST.get('quantity') is '': 
        product = Product.objects.get(pk=id)
        form = ReviewForm()
        messages.error(request, "Please enter a quantity to add product to cart!")
        return render(request, 'product.html', {'product': product, 'form':form })
    else:
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        if id in cart:
            cart[id] = int(cart[id]) + quantity      
        else:
            cart[id] = cart.get(id, quantity) 
    
        request.session['cart'] = cart
        return redirect(reverse('index'))
        
        
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))