from django.shortcuts import get_object_or_404, render
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from .cart import Cart
# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cartpage.html', {'cart': cart})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cartqty = cart.__len__()
        cart.add(product= product, qty=product_qty)
        response = JsonResponse({'qty':cartqty})

        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)

        basketqty = cart.__len__()
        baskettotal = cart.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id, qty=product_qty)

        basketqty = cart.__len__()
        baskettotal = cart.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response

def checkout(request):
    cart = Cart(request)
    return render(request, 'checkout.html', {'cart': cart})

def payment_confirm(request):
    return render(request, 'confirm.html')

def about(request):
    return render(request, 'About.html')