from django.shortcuts import render

order_items = []
for _ in range(3):
    order_items.append(
        {
            'title': 'Oranges',
            'price': '2.99',
            'image': 'img/fruite-item-1.jpg',
        }
    )

# Display new order view
def order_create(request):
    context = {'cart': order_items}
    return render(request, 'cart.html', context)


# Display a specific order details 
def order_show(request):
    context = {'cart': order_items}
    return render(request, 'checkout.html', context)
