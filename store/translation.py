from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, ProductTag

class BaseTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'description')
    required_languages = ('en', 'ka')


@register(Category)
class CategoryTranslationOptions(BaseTranslationOptions):
    pass

@register(Product)
class ProductTranslationOptions(BaseTranslationOptions):
    fields = ('origin', 'quality')

@register(ProductTag)
class ProductTagTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('en', 'ka')


