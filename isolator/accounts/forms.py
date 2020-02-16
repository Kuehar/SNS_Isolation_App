from django import forms
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.Form):
    """ユーザー登録フォーム"""
    email = forms.CharField(
        label='E-Mail',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':"",'class': 'input-age'})
    )

    password = forms.CharField(
        label='password',
        min_length=8,
        max_length=20,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input-height'})
    )


class SigninForm(AuthenticationForm):
    """ユーザーログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label