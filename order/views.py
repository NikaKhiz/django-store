from django.shortcuts import HttpResponse


# Display new order view
def order_create(request):
    return HttpResponse('order creation view')


# Display a specific order details 
def order_show(request, id):
    return HttpResponse(f'details for order - {id}')
