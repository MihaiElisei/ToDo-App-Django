from django import forms
from .models import Item

# create new item forom and get functionality from django models form


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']

