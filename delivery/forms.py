from django import forms

from delivery.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
