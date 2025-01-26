import re

from django import forms
from django.contrib.auth.forms import (
    PasswordResetForm,
    UserChangeForm,
    UserCreationForm,
)
from django.core.exceptions import ValidationError

from diary.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        # fields = ("email", "password1", "password2",)
        fields = (
            "email",
            "phone",
            "country",
            "avatar",
            "password1",
            "password2",
        )

    def clean_phone(self):
        cleaned_data = self.cleaned_data["phone"]
        for cleaned_data in cleaned_data.split(","):
            phone = re.sub(r"[\s +.()\-]", "", cleaned_data)
            if not phone:
                continue
            if not phone.isdigit():
                raise ValidationError("Можно использовать только цифры.")
            if len(phone) == 11:
                pass
            elif len(phone) == 10:
                phone = "7" + phone
            else:
                raise ValidationError("Проверьте количество цифр.")
            cleaned_data = phone
        return cleaned_data

    def clean_country(self):
        cleaned_data = self.cleaned_data["country"]
        for country in cleaned_data.split(","):
            if country.isdigit():
                raise ValidationError("Можно использовать только буквы.")
            cleaned_data = country
        return cleaned_data


class ResetPasswordForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = [
            "email",
        ]


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "avatar",
            "country",
        ]

    def clean_phone(self):
        cleaned_data = self.cleaned_data["phone"]
        for cleaned_data in cleaned_data.split(","):
            phone = re.sub(r"[\s +.()\-]", "", cleaned_data)
            if not phone:
                continue
            if not phone.isdigit():
                raise ValidationError("Можно использовать только цифры.")
            if len(phone) == 11:
                pass
            elif len(phone) == 10:
                phone = "7" + phone
            else:
                raise ValidationError("Проверьте количество цифр.")
            cleaned_data = phone
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()
        if self.instance and self.instance.pk:
            # Делаем поле email недоступным для редактирования
            self.fields["email"].disabled = True
