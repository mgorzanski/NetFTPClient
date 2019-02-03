"""
Definition of forms.
"""

from django import forms

class ConnectionForm(forms.Form):
    server = forms.CharField(label='Serwer', required=True)
    username = forms.CharField(label='Nazwa użytkownika', required=False)
    password = forms.CharField(label='Hasło', required=False, widget=forms.PasswordInput)
    port = forms.CharField(label='Port', required=False, widget=forms.NumberInput)
