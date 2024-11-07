from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _

class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('name'))
    slug = models.SlugField(unique=True, max_length=200, verbose_name=_('slug')) 
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategory', verbose_name=_('parent'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name=_('image'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('date update'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('date creation'))
    
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _('categories')
        
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('name'))
    slug = models.SlugField(unique=True, max_length=200, verbose_name=_('slug')) 
    description = models.TextField(null=True, blank=True, verbose_name=_('description'))
    price = models.DecimalField(default=1, max_digits=10, decimal_places=2, null=False, verbose_name=_('price'))
    quantity = models.PositiveIntegerField(default=1, blank=True, null=True, verbose_name=_('quantity'))
    weight = models.PositiveIntegerField(default=1, null=True, blank=True, verbose_name=_('weight'))
    origin = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('origin'))
    quality = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('quality'))
    healthy = models.BooleanField(default=True, verbose_name=_('healthy'))
    is_published = models.BooleanField(default=False, verbose_name=_('is published'))
    image = models.ImageField(upload_to='products/', null=False, blank=False, verbose_name=_('image'))
    category = models.ManyToManyField('store.Category', related_name='products', verbose_name=_('category'))
    tag = models.ManyToManyField('store.ProductTag', related_name='products', verbose_name=_('tag'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('date update'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('date creation'))
    
    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('name'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('date update'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('date creation'))

    class Meta:
        verbose_name = _("product tag")
        verbose_name_plural = _('produtc tags')

    def __str__(self):
        return self.name