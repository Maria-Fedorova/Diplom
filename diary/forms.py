from django import forms
from django.forms import BooleanField

from diary.models import Diary


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class DiaryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Diary
        exclude = ("author",)


class DiarySearchForm(forms.Form):
    query = forms.CharField(label="Поиск", max_length=150, widget=forms.TextInput(attrs={"placeholder": "Поиск"}))
