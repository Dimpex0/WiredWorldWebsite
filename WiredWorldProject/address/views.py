from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from WiredWorldProject.account.models import Profile
from WiredWorldProject.address.forms import AddressCreationForm
from WiredWorldProject.address.models import Address


class CreateAddressView(views.CreateView):
    model = Address
    template_name = 'address/create.html'
    form_class = AddressCreationForm

    def get_success_url(self):
        return redirect('cart page')

    def form_valid(self, form):
        profile = Profile.objects.get(client=self.request.user)
        street = form.cleaned_data['street']
        city = form.cleaned_data['city']
        state = form.cleaned_data['state']
        postal_code = form.cleaned_data['postal_code']
        country = form.cleaned_data['country']
        Address.objects.create(profile=profile, street=street, city=city, state=state, postal_code=postal_code, country=country)
        return self.get_success_url()


class UpdateAddressView(views.UpdateView):
    model = Address
    template_name = 'address/update.html'
    success_url = reverse_lazy('cart page')
    fields = ['street', 'city', 'state', 'postal_code', 'country']

    def get_object(self, queryset=None):
        return Address.objects.get(profile__client=self.request.user)
