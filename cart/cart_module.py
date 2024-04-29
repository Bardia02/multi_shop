from product.models import Product



CART_SESSION_ID="cart"

class Cart:
    def __init__(self,request):
        self.session=request.session

        cart=self.session.get(CART_SESSION_ID)
        if not cart:
            cart=self.session[CART_SESSION_ID]={}
        self.cart=cart
        print(type(self.session))


    def __iter__(self):
        cart=self.cart.copy()

        for item in cart.values():
            product=Product.objects.get(id=int(item['id']))
            item['product']=Product.objects.get(id=int(item['id']))
            item['total']=int(item['quantity'])*int(item['price'])
            item['unique_id']=self.unicue_id_generator(product.id,item['color'],item['size'])
            yield item

    def unicue_id_generator(self,id,color,size):
        result=f"{id}-{color}-{size}"
        return result

    def remove_cart(self):
        del self.session[CART_SESSION_ID]

    def add(self,product,color,size,quantity):
        unique=self.unicue_id_generator(product.id,color,size)
        if unique not in self.cart:
            self.cart[unique]={"quantity":0,"price":str(product.price),'color':color,'size':size,'id':product.id}

        self.cart[unique]['quantity']+=int(quantity)
        self.save()
    def total(self):
        cart=self.cart.values()
        total=sum(int(item['quantity'])*int(item['price']) for item in cart)
        # for item in cart:
        #     total+=item['total']
        return total
    def delete(self,id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def save(self):
        self.session.modified = True