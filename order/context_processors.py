from django.db.models import Sum
from .models import UserCart

def cart_items_context(request):
    total_products = 0
    if request.user.is_authenticated:
        cart = UserCart.objects.filter(user=request.user).first()
        if cart:
            total_products = cart.cart_items.aggregate(total=Sum('quantity'))['total'] or 0

    return {
        'total_products': total_products,
    }
