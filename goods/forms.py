from django import forms
from goods.models import Products


class CustomProductCreationForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

