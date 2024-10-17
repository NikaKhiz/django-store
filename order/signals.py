from django.db.models.signals import post_save
from django.dispatch import receiver
from userapp.models import CustomUser  
from order.models import Usercart

@receiver(post_save, sender=CustomUser)
def create_user_cart(sender, instance, created, **kwargs):
    if created:  
        Usercart.objects.create(user=instance)
