from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic as views

from WiredWorldProject.address.models import Address
from WiredWorldProject.cart.models import Cart
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
