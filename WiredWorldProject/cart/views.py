from django.shortcuts import render
from django.views import generic as views

from WiredWorldProject.account.models import Profile
from WiredWorldProject.address.models import Address
from WiredWorldProject.cart.models import Cart


class CartView(views.ListView):
    model = Cart
    template_name = 'cart/index.html'

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



