from django.shortcuts import render, redirect

from WiredWorldProject.account.models import Profile
from WiredWorldProject.cart.models import Cart
from WiredWorldProject.order.models import Order


def order_history_page(request):
    context = {}
    if Order.objects.filter(profile__client=request.user).exists():
        orders_table = []
        last_seen_date = ''
        orders = Order.objects.filter(profile__client=request.user).order_by('-date')
        for order in orders:
            if order.date != last_seen_date:
                orders_table.append([])
                last_seen_date = order.date
            orders_table[-1].append(order)
        context['orders_table'] = orders_table
    return render(request, 'order/index.html', context=context)


def place_order_again(request, date):
    profile = Profile.objects.get(client=request.user)
    carts = Cart.objects.filter(profile__client=request.user)
    orders = Order.objects.filter(profile__client=request.user, date=date)
    cart_products = []
    if carts.exists():
        for cart in carts:
            cart_products.append(cart.product)

    for order in orders:
        product_stock = order.product.stock
        if order.product in cart_products:
            cart = Cart.objects.get(profile=profile, product=order.product)
            if product_stock <= 0:
                continue
            if cart.quantity + order.quantity >= product_stock:
                cart.quantity = product_stock
                cart.save()
                continue
            cart.quantity += order.quantity
            cart.save()
        else:
            Cart.objects.create(profile=profile, product=order.product, quantity=order.quantity)

    return redirect('cart page')
