# Import libraries and models
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Provide stripe api key
stripe.api_key = settings.STRIPE_SECRET

# User checkout
@login_required()
def checkout(request):
    # Create checkout form instances
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        # Validate checkout forms
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            # Get cart session
            cart = request.session.get('cart', {})
            total = 0
            # Get cart items for checkout
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()
            # Attempt payment via stripe
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            # Inform user if card declined
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            # Inform user of successful payment
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('index'))
            # Inform user that payment not successful
            else:
                messages.error(request, "Unable to take payment")
        # Inform user that payment not possible with card
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    # Reshow checkout forms
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    # Render checkout form
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
    
    
    