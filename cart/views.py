# Import libraries and forms
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from products.models import Product
from customer_reviews.forms import ReviewForm
from django.contrib import messages

# View cart
def view_cart(request):
    # Render cart contents page
    return render(request, "cart.html")

# Add items to cart
def add_to_cart(request, id):
    # Add quantity of product to cart
    if request.POST.get('quantity') is '':
        # Get product object
        product = Product.objects.get(pk=id)
        # Get instance of form
        form = ReviewForm()
        # Inform user of error
        messages.error(request, "Please enter a quantity to add product to cart!")
        # Return user to product page
        return render(request, 'product.html', {'product': product, 'form':form })
    # If product quantity is valid value
    else:
        # Get quantity from form
        quantity = int(request.POST.get('quantity'))
        # Get session object
        cart = request.session.get('cart', {})
        # If product in cart edit quantity
        if id in cart:
            cart[id] = int(cart[id]) + quantity
        # If product not in cart add to cart
        else:
            cart[id] = cart.get(id, quantity) 
        # Assign cart to session cart
        request.session['cart'] = cart
        # Search for product id
        product = Product.objects.get(id=id)
        # Inform user of successful add to cart
        messages.success(request, "This product has been added to your cart!")
        # Return to product page
        return HttpResponseRedirect(reverse('product', args=(product.id,)))
        
# Edit cart quantity of product        
def adjust_cart(request, id):
    # Adjust the quantity of product 
    if request.POST.get('quantity') is '':
        # Inform user that no quantity entered
        messages.error(request, "Please enter a quantity to add amend cart!")
        # Return user to cart
        return redirect(reverse('view_cart'))
    # Get amended quantity from cart
    else:
        quantity = int(request.POST.get('quantity'))
        # Get session cart
        cart = request.session.get('cart', {})
        # Adjust cart value to new quantity
        if quantity > 0:
            cart[id] = quantity
        # If quantity none remove product from cart
        else:
            cart.pop(id)
        # Get session cart
        request.session['cart'] = cart
        # Render user cart
        return redirect(reverse('view_cart'))
        