from django.db import models


class Usercart(models.Model):
    user = models.OneToOneField("userapp.CustomUser", on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    coupon_code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username
    


class CartItem(models.Model):
    cart = models.ForeignKey('order.Usercart', on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, related_name='cart_products')
    quantity = models.PositiveIntegerField(default=1, null=False, blank=True)
    action = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"cart of {self.cart.user.username}"

    class Meta:
        unique_together = ('cart', 'product')  
