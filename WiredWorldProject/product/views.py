from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.dispatch import Signal
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.html import strip_tags
from django.views import generic as views
from django.contrib import messages

from WiredWorldProject import settings
from WiredWorldProject.account.models import Profile
from WiredWorldProject.cart.models import Cart
from WiredWorldProject.like.models import Like
from WiredWorldProject.product.forms import ProductCreateForm
from WiredWorldProject.product.models import Product, Category, SubCategory
from WiredWorldProject.product.signals import update_product_signal


def get_user_groups_permissions(user, groups: list):
    """
    :param user: gets the current user
    :param groups: gets groups that will be checked for the user
    :return: returns True if all the user belongs to all groups, else return False
    """
    for group in groups:
        try:
            group_permissions = Group.objects.get(name=group).permissions.all()
            for permission in group_permissions:
                if not user.has_perm(permission):
                    return False
        except Exception:
            return False
    return True


class IndexView(views.ListView):
    model = Product
    template_name = 'index.html'
    ordering = '-pk'
    paginate_by = 16

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and get_user_groups_permissions(self.request.user, ['Product management']):
            context['product_manager'] = True
            context['product_form'] = ProductCreateForm
        context['categories'] = Category.objects.all()
        if self.request.user.is_authenticated:
            likes = Like.objects.filter(profile__client=self.request.user)
            context['liked_products'] = [like.product for like in likes]
        return context

    def post(self, request):
        if 'product-form' in request.POST:
            form = ProductCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product has been added!')
            else:
                if form.has_error('image'):
                    messages.error(request, 'Invalid image type')
                if form.has_error('title'):
                    messages.error(request, 'Invalid title')
                if form.has_error('description'):
                    messages.error(request, 'Invalid description')
                if form.has_error('price'):
                    messages.error(request, 'Invalid price')
                if form.has_error('stock'):
                    messages.error(request, 'Invalid stock number')

        elif 'category-form' in request.POST:
            if request.POST['category-form'] != '':
                return redirect('category page', category=request.POST['category-form'])
        return redirect('home page')


class EditProductView(LoginRequiredMixin, views.UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'product/edit.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        domain = self.request.get_host()
        update_product_signal.send(sender=Product, instance=Product.objects.get(pk=self.kwargs['pk']), domain=domain, new_stock=form.cleaned_data['stock'])
        return super().form_valid(form)


class DetailsProductView(views.DetailView):
    model = Product
    template_name = 'product/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['liked'] = Like.objects.filter(profile__client=self.request.user, product=self.object)
        if self.request.user.is_authenticated and get_user_groups_permissions(self.request.user, ['Product management']):
            context['product_manager'] = True
            context['product_form'] = ProductCreateForm
        return context

    def post(self, request, pk):
        if request.user.is_authenticated:
            quantity = 1 if request.POST['quantity'] == "" else int(request.POST['quantity'])
            profile = Profile.objects.get(client=request.user)
            product = Product.objects.get(pk=pk)
            if Cart.objects.filter(profile=profile, product=product):
                cart = Cart.objects.get(profile=profile, product=product)
                cart.quantity += quantity
                cart.save()
                if cart.quantity > product.stock:
                    cart.quantity = product.stock
                    cart.save()
                    messages.error(request, "Can't add more of this item (not enough stock)")
                    return redirect('details product page', pk=pk)
                messages.success(request, 'Successfully added to cart')
            else:
                cart = Cart.objects.create(profile=profile, product=product, quantity=quantity)
                if cart.quantity > product.stock:
                    cart.quantity = product.stock
                    cart.save()
                    messages.error(request, "Can't add more of this item (not enough stock)")
                    return redirect('details product page', pk=pk)
                messages.success(request, 'Successfully added to cart')
            return redirect('details product page', pk=pk)
        else:
            return redirect('login page')


class CategoryView(views.ListView):
    model = Category
    template_name = 'product/category.html'
    paginate_by = 16
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        if self.request.GET:
            selected = []
            for key, value in self.request.GET.items():
                selected.append(value)
            context['selected_subcategories'] = selected
        if self.request.user.is_authenticated and get_user_groups_permissions(self.request.user, ['Product management']):
            context['product_manager'] = True
        context['current_category'] = self.kwargs['category']
        context['subcategories'] = SubCategory.objects.filter(category__name=self.kwargs['category'])
        if self.request.user.is_authenticated:
            likes = Like.objects.filter(profile__client=self.request.user)
            context['liked_products'] = [like.product for like in likes]
        return context

    def get_queryset(self):
        if self.request.GET:
            selected = []
            for key, value in self.request.GET.items():
                selected.append(value)
            products = Product.objects.filter(category__name__in=selected)
            return products
        products = Product.objects.filter(category__category__name=self.kwargs['category']).order_by('-pk')
        return products
