from django.urls import path

from WiredWorldProject.cart.views import CartView, remove_item_view, update_quantity_view, process_order_view

urlpatterns = [
    path('', CartView.as_view(), name='cart page'),
    path('remove-item/<int:pk>/', remove_item_view, name='remove item from cart'),
    path('update-quantity/<int:pk>/', update_quantity_view, name='update cart item quantity'),
    path('process/', process_order_view, name='process order'),
]
