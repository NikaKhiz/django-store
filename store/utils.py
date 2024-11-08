from django.db.models import Count
from order.models import CartItem
from store.models import Product


def get_top_rated_product(limit):
    cart_items = (
            CartItem.objects
            .select_related('product')
            .values('product')
            .annotate(user_count=Count('cart__user', distinct=True))
            .order_by('-user_count')
            [:limit]
        )
    
    products = Product.objects.filter(id__in=[item['product'] for item in cart_items]).prefetch_related('tag').annotate(user_count=Count('cart_products__cart__user'))
    return products
