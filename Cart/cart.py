from django.conf import settings
from store.models import *

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
    
    def __iter__(self):
        product_ids = self.cart.keys()
        
        product_cleaned_ids = []
        
        for p in product_ids:
            product_cleaned_ids.append(p)
            
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
            
        
        for item in self.cart.values():
            print(item)
           
            ## issue here ## 

            if item['sale_price']:
                item['total_price'] = float(item['sale_price']) * int(item['quantity'])
            else:
                item['total_price'] = float(item['market_price']) * int(item['quantity'])
                
                print(item['total_price'])

       
            yield item
            
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    
        
    def add(self, product, quantity=1, updated_quantity=False):
        product_id = str(product.id)
        market_price = product.market_price
        sale_price = product.sale_price

        if sale_price:
            if product_id not in self.cart:
                self.cart[product_id] = {'quantity':0, 'sale_price': sale_price, 'id': product_id}
            
            if updated_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
        else:
            if product_id not in self.cart:
                self.cart[product_id] = {'quantity':0, 'market_price': market_price, 'id': product_id}
            
            if updated_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1
        self.save()
        
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
        
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    


    def save(self):
        print("saves")
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modfied = True
        


    def get_total_length(self):
            return sum(int(item['quantity']) for item in self.cart.values())
    
    def get_total_cost(self):
        return sum(float(item['total_price']) for item in self)
    
 
