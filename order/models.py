from django.db import models


class Usercart(models.Model):
    user = models.OneToOneField("userapp.CustomUser", on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    coupon_code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def checkout_total(self):
        total = sum(item.total_price for item in self.cart_items.all())

        if self.discount_code:
            # dynamic value for discount in future
            total *= 0.85

        return total


class CartItem(models.Model):
    cart = models.ForeignKey(Usercart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=False, blank=True)

    def __str__(self):
        return f"cart of {self.cart.user.username}"

    @property
    def total_price(self):
        return self.quantity * self.product.price
    
    @property
    def item_name(self):
        return self.product.name

    @property
    def item_image(self):
        return self.product.image.url
    
    class Meta:
        unique_together = ('cart', 'product')
