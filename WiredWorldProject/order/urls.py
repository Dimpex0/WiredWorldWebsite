from django.urls import path

from WiredWorldProject.order.views import order_history_page, place_order_again

urlpatterns = [
    path('history/', order_history_page, name='orders history page'),
    path('place-again/<date>/', place_order_again, name='place order again'),
]
