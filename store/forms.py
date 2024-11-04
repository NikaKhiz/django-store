from django import forms

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=255, required=False)
    product_price = forms.IntegerField(required=False)
    product_tag = forms.CharField(max_length=255, required=False)
    product_sort_list = forms.ChoiceField(choices=[
        ('price_up', 'Price Up'),
        ('price_down', 'Price Down'),
        ('created_at', 'Created At'),
    ], required=False)


class SendEmailForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(min_length=20, required=True)