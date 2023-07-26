from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from WiredWorldProject.product.api import ProductListApiView
from WiredWorldProject.product.views import IndexView, EditProductView, DetailsProductView, CategoryView

urlpatterns = [
    path('', cache_page(15 * 60)(IndexView.as_view()), name='home page'),
    path('edit/<int:pk>/', EditProductView.as_view(), name='edit product page'),
    path('details/<int:pk>/', DetailsProductView.as_view(), name='details product page'),
    path('products-api/', ProductListApiView.as_view(), name='api list products'),
    path('category/<str:category>/', CategoryView.as_view(), name='category page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
