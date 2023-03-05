from django.forms import ModelForm, models

from _old_product.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']