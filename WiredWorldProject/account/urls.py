from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView, LoginView, DetailsAccountView, DeleteProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register page'),
    path('login/', LoginView.as_view(), name='login page'),
    path('details/', DetailsAccountView.as_view(), name='account details page'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('delete/', DeleteProfileView.as_view(), name='delete profile page'),
    path('password-reset/', PasswordResetView.as_view(template_name='account/password-reset.html', html_email_template_name='emails/password_reset_email.html'), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='account/password-reset-done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='account/password-reset-confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='account/password-reset-complete.html'), name='password_reset_complete'),
]

from .signals import *
