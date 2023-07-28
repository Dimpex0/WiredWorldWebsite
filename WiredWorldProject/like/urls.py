from django.urls import path

from WiredWorldProject.like.views import like_product, unlike_product, LikeListView

urlpatterns = [
    path('', LikeListView.as_view(), name='liked page'),
    path('like/<int:pk>', like_product, name='like product'),
    path('unlike/<int:pk>', unlike_product, name='unlike product'),
]
