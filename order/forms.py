from django import forms
from .models import CartItem, Usercart
from django.core.exceptions import ValidationError 

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity', 'action']

    def __init__(self, *args, product, **kwargs):
        super().__init__(*args, **kwargs)
        self.product = product


    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity') or 1

        if quantity > self.product.quantity:
            raise ValidationError('not enough products!')

        return cleaned_data
    
    def update_cart_item(self, user):
        cleaned_data = self.cleaned_data
        quantity = cleaned_data['quantity']
        action = cleaned_data['action']

        cart = Usercart.objects.get(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=self.product)

        if action == 'add':
            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity

        elif action == 'decrease':
            cart_item.quantity -= quantity
            if cart_item.quantity <= 0:
                cart_item.delete()
                return None  
            
        elif action == 'delete':
            cart_item.delete()
            return None  

        cart_item.save()
        return cart_item
