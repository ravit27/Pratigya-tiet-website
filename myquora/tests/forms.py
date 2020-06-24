from django import forms


class contact(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    mob = forms.CharField(max_length=13)
    content = forms.CharField(max_length=500)