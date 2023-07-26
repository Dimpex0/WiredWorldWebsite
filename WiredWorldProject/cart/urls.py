from django.urls import path

from WiredWorldProject.cart.views import CartView

urlpatterns = [
    path('', CartView.as_view(), name='cart page'),
]
