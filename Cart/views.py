from django.shortcuts import render
from Cart.cart import *
from django.conf import settings

# Create your views here.


def cart_details(request):
    cart = Cart(request)
   
    productString = ""
    
    for item in cart:
        product = item['product']

        url = '%s/%s/' % (product.category.id, product.id)

        if product.sale_price:
            b = "{'id':'%s','title':'%s','sale_price':'%s','quantity':'%s', 'total_price':'%s', 'thumbnail':'%s', 'url':'%s'},"%(product.id, product.title, product.sale_price, item['quantity'], item['total_price'], product.get_thumbnail(), url)
        
            productString = productString + b
        else:
             b = "{'id':'%s','title':'%s','market_price':'%s','quantity':'%s', 'total_price':'%s', 'thumbnail':'%s', 'url':'%s'},"%(product.id, product.title, product.market_price, item['quantity'], item['total_price'], product.get_thumbnail, url)

             productString = productString + b
    context = {
        'cart': cart,
        'productString': productString,
        
    }
    
    return render(request, 'cart.html', context)