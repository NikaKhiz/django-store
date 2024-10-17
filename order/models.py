from django.db import models


class Usercart(models.Model):
    user = models.OneToOneField("userapp.CustomUser", on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return self.user.username

    