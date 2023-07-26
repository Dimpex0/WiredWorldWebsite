from django import forms

from WiredWorldProject.product.models import Product


class ProductCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title...'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description...'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price...'
            }),
            'stock': forms.NumberInput(attrs={
                'placeholder': 'Stock...'
            })
        }
