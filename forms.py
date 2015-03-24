from django import forms

class AddItemForm(forms.Form):
    item_name = forms.CharField()

