from django.urls import path

from WiredWorldProject.address.views import CreateAddressView, UpdateAddressView

urlpatterns = [
    path('add/', CreateAddressView.as_view(), name='add address page'),
    path('update/', UpdateAddressView.as_view(), name='update address page')
]
