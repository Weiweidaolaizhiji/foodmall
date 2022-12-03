from django import forms

class LoginForm(forms.Form):
    user = forms.EmailField(required=True)
    pwd = forms.CharField(required=True,min_length=8,max_length=16)
