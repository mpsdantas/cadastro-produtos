from django import forms
from .models import Produto
class ProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','descricao']