from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class addAccount(forms.Form):
    name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    host = forms.CharField(max_length=200)
    port = forms.CharField(max_length=200)
    key_1 = forms.CharField(max_length=200)
    key_2 = forms.CharField(max_length=200)
    key_3 = forms.CharField(max_length=200)

class updateAccount(forms.Form):
    name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    host = forms.CharField(max_length=200)
    port = forms.CharField(max_length=200)
    key_1 = forms.CharField(max_length=200)
    key_2 = forms.CharField(max_length=200)
    key_3 = forms.CharField(max_length=200)

class Accounts(forms.Form):
    accounts_detail = forms.CharField(label='Anything', max_length=100)

class Tag(forms.Form):
    tag_name = forms.CharField(label='Anything', max_length=100)
    tag_number = forms.CharField(label='Anything', max_length=100)

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
