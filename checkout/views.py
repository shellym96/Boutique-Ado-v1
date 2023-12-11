from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order-form': order_form,
        'stripe_public_key': 'pk_test_51OM9dxBcXVF7OF7TsVqUpwXWOaqCXnHetj7Hw2yhzevrnJSGHAJPHaRwTiOQu4KFbjk4I6f171auAY005py3Qo2500ePCgpxYd'
    }

    return render(request, template, context)
