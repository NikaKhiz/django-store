from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product
from .forms import CartItemForm
from .models import Usercart
from django.db.models import F, Sum

order_items = []
for _ in range(3):
    order_items.append(
        {
            'title': 'Oranges',
            'price': '2.99',
            'image': 'img/fruite-item-1.jpg',
        }
    )


# Display the cart view
@login_required
def order_create(request):
    cart, _ = Usercart.objects.get_or_create(user=request.user)
    cart_items = cart.cart_items.all().annotate(total_price=F('product__price') * F('quantity'))

    shipping_cost = 3
    subtotal = sum(item.total_price for item in cart_items)
    total = subtotal + shipping_cost

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total': total,
        'shipping_cost': shipping_cost
        }
    
    return render(request, 'cart.html', context)

# Display the checkout view
@login_required
def order_show(request):
    cart, _ = Usercart.objects.get_or_create(user=request.user)
    cart_items = cart.cart_items.all().annotate(total_price=F('product__price') * F('quantity'))

    shipping_cost = 3  
    subtotal = sum(item.total_price for item in cart_items)
    total = subtotal + shipping_cost

    context = {
        'cart': cart_items,
        'subtotal': subtotal,
        'total': total,
        'shipping_cost': shipping_cost,
    }
    
    return render(request, 'checkout.html', context)


@login_required
def cart_actions(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    form = CartItemForm(request.POST, product=product)

    if form.is_valid():
        form.update_cart_item(request.user)
    else:
        return HttpResponse('Invalid input values', status=400)

    referer = request.META.get('HTTP_REFERER', 'order:cart')
    return redirect(referer)
