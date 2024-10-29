from django.db.models import Sum
from .models import Usercart

def cart_items_context(request):
    cart = None
    if request.user.is_authenticated:
        cart = Usercart.objects.filter(user=request.user).first()
    total_products = cart.cart_items.aggregate(total=Sum('quantity'))['total'] if cart else 0

    return {
        'total_products': total_products,
    }
