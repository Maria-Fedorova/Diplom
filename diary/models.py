from django.db import models

from users.models import User


class Diary(models.Model):
    """
    Описание класса дневника.
    ...
    Поля
    ________
    title - Заголовок.
    content - Содержание записи.
    create_date - Дата создания, формируется автоматически.
    updated_date - Дата обновления записи, формируется автоматически.
    author - Пользователь, автор записи. Каскадное удаление пользователя и всех его записей.
    """

    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание записи")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
       User, verbose_name="Владелец", on_delete=models.CASCADE, blank=True, null=True
   )

    class Meta:
        verbose_name = "Запись в дневнике"
        verbose_name_plural = "Записи в дневнике"
        ordering = ("create_date",)

    def __str__(self):
        return self.title
