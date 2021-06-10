import json
from django.http import JsonResponse
from Cart.cart import Cart
from django.shortcuts import get_object_or_404

from store.models import *
from order.utils import *


def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}

    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, updated_quantity=False, quantity=1)
    else:
        cart.add(product=product, updated_quantity=True, quantity=quantity)

    
    return JsonResponse(jsonresponse)


## Function For Remove Cart

def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}

    product_id = str(data['product_id'])

    cart = Cart(request)

    cart.remove(product_id)


    return JsonResponse(jsonresponse)


def api_checkout(request):
    data = json.loads(request.body)
    cart = Cart(request)
    jsonresponse = {'success': True}

    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    zipcode = data['zipcode']
    city = data['city']

    orderId = checkout(request, first_name, last_name, email, address, zipcode, city)

    paid = True

    if paid == True:
        order = Order.objects.get(pk=orderId)
        order.paid = True
        order.paid_amount = cart.get_total_cost()

        order.save()
        cart.clear()

    return JsonResponse(jsonresponse)



