import random
import secrets
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import ResetPasswordForm, UserProfileForm, UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    """
    Создание пользователя.
    """

    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """
        Валидация создания пользователя.
        """
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/user/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейдите по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """
    Верификации почты.
    """
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserResetPasswordView(PasswordResetView):
    """
    Сброс пароля.
    """

    form_class = ResetPasswordForm
    template_name = "users/reset_password.html"
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        """
        Валидация сброса пароля.
        """
        email = form.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            if user:
                password = "".join(
                    [
                        random.choice(string.digits + string.ascii_letters)
                        for i in range(0, 10)
                    ]
                )
                user.set_password(password)
                user.is_active = True
                user.save()
                send_mail(
                    subject="Сброс пароля",
                    message=f" Ваш новый пароль {password}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email],
                )
            return redirect(reverse("users:login"))
        except User.DoesNotExist:
            return redirect(reverse("users:register"))


class ProfileView(UpdateView):
    """
    Просмотр профиля
    """

    model = User
    form_class = UserProfileForm
    template_name = "users/user_profile.html"
    success_url = reverse_lazy("diary:diary_list")

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """
    Редактирование профиля
    """

    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("diary:diary_list")

    def get_object(self, queryset=None):
        return self.request.user
