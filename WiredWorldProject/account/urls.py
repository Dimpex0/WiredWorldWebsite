from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView, LoginView, DetailsAccountView, DeleteProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register page'),
    path('login/', LoginView.as_view(), name='login page'),
    path('details/', DetailsAccountView.as_view(), name='account details page'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('delete/', DeleteProfileView.as_view(), name='delete profile page')
]

from .signals import *
