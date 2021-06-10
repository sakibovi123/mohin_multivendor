import os
import datetime

from order.models import *
from Cart.cart import Cart


def checkout(request, first_name, last_name, email, address, zipcode, city):
    order = Order(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, city=city)
    
    if request.user.is_authenticated:
    	order.user = request.user

    order.save()
    
    cart = Cart(request)
    
    for item in cart:
        if item['sale_price']:
            OrderItems.objects.create(order=order, product=item['product'], sale_price=item['sale_price'], quantity=item['quantity'])
        else:
            OrderItems.objects.create(order=order, product=item['product'], market_price=item['market_price'], quantity=item['quantity'])
    return order.id