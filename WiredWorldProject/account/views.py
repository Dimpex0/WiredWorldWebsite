from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib import messages

from WiredWorldProject.account.forms import ClientRegisterForm, ProfileUpdateForm, ClientLoginForm
from WiredWorldProject.account.models import Profile

UserModel = get_user_model()


class RegisterView(views.CreateView):
    model = UserModel
    template_name = 'account/register.html'
    form_class = ClientRegisterForm

    def get_success_url(self):
        return reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginView(auth_views.LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home page')
    form_class = ClientLoginForm

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or self.get_default_redirect_url()


class DetailsAccountView(LoginRequiredMixin, views.UpdateView):
    model = Profile
    template_name = 'account/details.html'
    form_class = ProfileUpdateForm

    def get_object(self, queryset=None):
        return Profile.objects.get(client=self.request.user)

    def form_valid(self, form):
        if form.has_changed():
            return super().form_valid(form)
        return self.get_success_url()

    def get_success_url(self):
        return reverse('account details page')


class DeleteProfileView(LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'account/delete.html'
    success_url = reverse_lazy('home page')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        if 'cancel' in self.request.POST:
            return redirect('home page')
        else:
            messages.success(self.request, 'Profile deleted successfully!')
            return super().form_valid(form)
