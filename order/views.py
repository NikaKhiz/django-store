from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product
from .forms import CartItemForm
from .models import Usercart
from django.db.models import F, Sum
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# parent view for cart and checkout views
class BaseCartView(LoginRequiredMixin, View):
    shipping_cost = 3 

    def get_cart_context(self, request):
        cart, _ = Usercart.objects.get_or_create(user=request.user)
        cart_items = cart.cart_items.all().annotate(total_price=F('product__price') * F('quantity'))

        subtotal = sum(item.total_price for item in cart_items)
        total = subtotal + self.shipping_cost

        return {
            'cart_items': cart_items,
            'subtotal': subtotal,
            'total': total,
            'shipping_cost': self.shipping_cost,
        }
    

class OrderCreateView(BaseCartView):
    template_name = 'cart.html'

    def get(self, request, *args, **kwargs):
        context = self.get_cart_context(request)
        return render(request, self.template_name, context)


class OrderShowView(BaseCartView):
    template_name = 'checkout.html'

    def get(self, request, *args, **kwargs):
        context = self.get_cart_context(request)
        # change cart_items key into cart for checkout template  
        context['cart'] = context.pop('cart_items') 
        return render(request, self.template_name, context)


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
