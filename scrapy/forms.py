import re

from django import forms

from .constants import NAME_ERROR, EMAIL_EXIST, NON_USER
from .models import User


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("name", "email", "password")

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if re.match(r'^[a-zA-Z]+$', name, re.I):
            return name

        raise forms.ValidationError(NAME_ERROR)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            User.objects.get(email=email)

            raise forms.ValidationError(EMAIL_EXIST)

        except User.DoesNotExist:

            return email
