from django import forms


class MyForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
