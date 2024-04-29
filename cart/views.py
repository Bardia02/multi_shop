from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .cart_module import Cart
from product.models import Product
from .models import Order, OrdrItem,DiscountCode


# Create your views here.


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_detail.html', {"cart": cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        size, color, quantity = request.POST.get("size", 'taksize'), request.POST.get("color",
                                                                                      'colorless'), request.POST.get(
            "quantity")
        # print(size,color,quantity)
        cart = Cart(request)
        cart.add(product, color, size, quantity)
        return redirect("cart:cart_detail")


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect("cart:cart_detail")


class OrderDetailView(View):
    def get(self,request,pk):
        order=get_object_or_404(Order,id=pk)
        return render(request,"cart/order_detail.html",{'order':order})


class OrderCreationView(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user,total_price=cart.total())
        for item in cart:
            OrdrItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'],
                                    quantity=item['quantity'], price=item['price'])
        cart.remove_cart()
        return redirect('cart:order_detail',order.id)


class ApplyDiscountView(View):
    def post(self,request,pk):
        code=request.POST.get('discount_code')
        order=get_object_or_404(Order,id=pk)
        discount_code=get_object_or_404(DiscountCode,name=code)
        if discount_code.quantity==0:
            return redirect('cart:order_detail',order.id)
        order.total_price-=(order.total_price * discount_code.discount)/100
        order.save()
        discount_code.quantity-=1
        discount_code.save()
        return redirect('cart:order_detail', order.id)