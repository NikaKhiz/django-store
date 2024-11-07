from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _




class CustomUser(AbstractUser):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must username")
        if not password:
            raise ValueError("Users must password")
            

        user = self.model(
            username=self.normalize_username(username),
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.create_user(
            username=self.normalize_username(username),
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    username=models.CharField(max_length=40,unique=True, verbose_name=_('username'))
    last_active_datetime = models.DateTimeField(auto_now=True, verbose_name=_('last active datetime'))
    email=models.EmailField(max_length=255,unique=True, verbose_name=_('email'))

    def __str__(self):
        return self.username

        
        