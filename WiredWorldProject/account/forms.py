from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm

from WiredWorldProject.account.models import Profile

UserModel = get_user_model()


class ClientLoginForm(AuthenticationForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''

    username = UsernameField(widget=forms.EmailInput(
        attrs={
            'placeholder': "Email",
            'id': 'email-input'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': 'password-input',
            'placeholder': 'Password'
        }
    ))


class ClientRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2')
        field_classes = {'username': UsernameField}
        widgets = {
            UserModel.USERNAME_FIELD: forms.TextInput(attrs={
                'placeholder': 'Email'
            }),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'image']
        widgets = {
            'image': forms.FileInput,
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            })
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'image': ''
        }
