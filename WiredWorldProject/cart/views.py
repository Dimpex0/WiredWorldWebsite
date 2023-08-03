import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import generic as views

from WiredWorldProject import settings
from WiredWorldProject.account.models import Profile
from WiredWorldProject.address.models import Address
from WiredWorldProject.cart.models import Cart
from WiredWorldProject.order.models import Order
from WiredWorldProject.product.models import Product


class CartView(views.ListView):
    model = Cart
    template_name = 'cart/index.html'
    ordering = 'pk'

    def get_queryset(self):
        return Cart.objects.filter(profile__client=self.request.user).order_by('pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for product in self.get_queryset():
            total += float(product.get_price())
        context['total_price'] = f"{total:.02f}"
        if Address.objects.filter(profile__client=self.request.user).exists():
            context['address'] = Address.objects.get(profile__client=self.request.user)
        return context


def remove_item_view(request, pk):
    product = Product.objects.get(pk=pk)
    cart = Cart.objects.get(profile__client=request.user, product_id=pk)
    cart.delete()
    messages.success(request, f'Removed {product.title} from cart')
    return redirect('cart page')


def update_quantity_view(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        cart = Cart.objects.get(profile__client=request.user, product_id=pk)
        quantity = int(request.POST['quantity'])
        if quantity <= 0:
            cart.delete()
            messages.success(request, f'Removed {product.title} from cart')
        else:
            cart.quantity = quantity
            cart.save()
    return redirect('cart page')


def process_order_view(request):
    time = datetime.datetime.now()
    time_formated = time.strftime("%d/%m/%Y %H:%M:%S")
    items_for_mail = []
    profile = Profile.objects.get(client=request.user)
    carts = Cart.objects.filter(profile__client=request.user)
    for cart in carts:
        items_for_mail.append(cart)
        Order.objects.create(profile=profile, product=cart.product, quantity=cart.quantity, date=time)
        if cart.product.stock - cart.quantity >= 0:
            cart.product.stock -= cart.quantity
            cart.product.save()
        cart.delete()

    html_message = render_to_string('emails/order.html', {
        'time': time_formated,
        'carts': items_for_mail,
        'address': Address.objects.get(profile__client=request.user)
    }
    )
    plain_message = strip_tags(html_message)
    send_mail(
        subject='Order placed successfully!',
        message=plain_message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    messages.success(request, 'Order placed successfully!')
    return redirect('home page')
