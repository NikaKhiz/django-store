from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategory')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        order_insertion_by = ['name']
    

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, max_length=200) 
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=1, max_digits=10, decimal_places=2, null=False)
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    weight = models.BigIntegerField(null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    quality = models.CharField(max_length=255, null=True, blank=True)
    healthy = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ManyToManyField('store.Category', related_name='products')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
