import os

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    field_order = [
        "username",
        "password1",
        "password2",
        "email",
        "first_name",
        "last_name",
        "age",
        "avatar",
    ]

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "age",
            "avatar",
        )
        field_classes = {"username": UsernameField}


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "age",
            "avatar",
        )
        field_classes = {"username": UsernameField}

    def clean_avatar(self):
        arg_as_str = "avatar"
        if arg_as_str in self.changed_data and self.instance.avatar:
            if os.path.exists(self.instance.avatar.path):
                os.remove(self.instance.avatar.path)
        return self.cleaned_data.get(arg_as_str)

    def clean_age(self):
        data = self.cleaned_data.get("age")
        if data:
            if data < 10 or data > 100:
                raise ValidationError(_("Please, enter a valid age!"))
        return data
