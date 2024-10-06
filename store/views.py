from django.shortcuts import HttpResponse


# Display provided products
def product_index(request):
    return HttpResponse('products list view')


# Display a specific product detail 
def product_show(request,id):
    return HttpResponse(f'details for product - {id}', )