from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Описание класса пользователя.
    ...
    Поля
    ________
    email - Email пользователя.
    phone - Телефон пользователя.
    country - Страна пользователя.
    avatar - Аватар пользователя.
    """
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=35, verbose_name="Телефон", blank=True, null=True,
                             help_text="Введите номер телефона")
    country = models.CharField(max_length=35, verbose_name="Страна", blank=True, null=True,
                               help_text="Введите название страны")
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Аватар", blank=True, null=True,
                               help_text="Загрузите аватар")
    token = models.CharField(
        max_length=100,
        verbose_name="Token",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
