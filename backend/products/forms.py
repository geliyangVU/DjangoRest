from django import forms

from .models import Product 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]

##here is an example of using django form class, Serializer class are similar