from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class LoginForm(forms.Form):
    # username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    # password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
