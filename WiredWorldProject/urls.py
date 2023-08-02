from django.contrib import admin
from django.core.mail import send_mail
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WiredWorldProject.product.urls')),
    path('account/', include('WiredWorldProject.account.urls')),
    path('review/', include('WiredWorldProject.review.urls')),
    path('cart/', include('WiredWorldProject.cart.urls')),
    path('order/', include('WiredWorldProject.order.urls')),
    path('address/', include('WiredWorldProject.address.urls')),
    path('like/', include('WiredWorldProject.like.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
