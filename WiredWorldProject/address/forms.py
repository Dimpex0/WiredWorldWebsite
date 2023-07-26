from django.forms import forms
from django.forms import ModelForm

from WiredWorldProject.address.models import Address


class AddressCreationForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'postal_code', 'country']
