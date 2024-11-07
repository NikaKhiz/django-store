from django.core.management import BaseCommand
from store.utils import get_top_rated_product
 
class Command(BaseCommand):
    help = 'gets mostly added products to carts by the most users.'

    def handle(self, *args, **kwargs):
        products = get_top_rated_product(limit=3).order_by('-user_count')

        self.stdout.write(self.style.SUCCESS("featured products added to carts by users:"))
        for product in products:
            self.stdout.write(f"{product.name}: added by {product.user_count} users")
