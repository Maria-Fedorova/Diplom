from django import forms
from django.forms import BooleanField, FileInput, ImageField

from diary.models import Diary


class StyleFormMixin:
    """
    Класс для добавления стилей к формам.
    По умолчания элементы BooleanField получают class "form-check-input",
    а все остальные поля получают class "form-control".
    Так же редактируется поле ImageField,
    так как по умолчанию отображается как текстовой поле, с чекбоксом,
    лишними надписями и ссылкой на изображение.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"

            elif isinstance(fild, ImageField):
                fild.widget = FileInput()
                fild.widget.attrs.update(
                    {"class": "form-control", "type": "file", "id": "formFile"}
                )
            else:
                fild.widget.attrs["class"] = "form-control"


class DiaryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Diary
        exclude = ("author",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Проверяем, редактируем ли мы существующую запись
        if self.instance and self.instance.pk:
            # Делаем поле title недоступным для редактирования
            self.fields["title"].disabled = True
