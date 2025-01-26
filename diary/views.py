from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from diary.forms import DiaryForm
from diary.models import Diary


class DiaryListView(ListView):
    """
    Представление списка всех записей пользователя.
    """

    model = Diary
    form_class = DiaryForm

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if self.request.user.is_authenticated:
            if query:
                queryset = queryset.filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                )
                form = DiaryForm()
            return queryset.filter(author=self.request.user)
        else:
            return Diary.objects.none()


class DiaryCreateView(LoginRequiredMixin, CreateView):
    """
    Создание новой записи в дневнике.
    """

    model = Diary
    form_class = DiaryForm
    success_url = reverse_lazy("diary:diary_list")

    def form_valid(self, form):
        """
        Проверяем, не повторяется ли заголовок новой записи у текущего пользователя.
        Если да, добавляем ошибку и возвращаем форму с ошибками.
        Если нет, сохраняем новую запись и переходим на страницу списка записей.
        """
        diary = form.save()
        user = self.request.user
        if Diary.objects.filter(author=user, title=diary.title).exists():
            form.add_error(None, "Запись уже существует")
            return self.form_invalid(form)
        else:
            diary.author = user
            diary.save()
            return super().form_valid(form)


class DiaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Diary
    form_class = DiaryForm
    success_url = reverse_lazy("diary:diary_list")

    def form_valid(self, form):
        """
        Сохраняем изменения в записи.
        """
        diary = form.save()
        user = self.request.user
        diary.author = user
        diary.save()
        return super().form_valid(form)


class DiaryDetailView(LoginRequiredMixin, DetailView):
    model = Diary


class DiaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Diary
    success_url = reverse_lazy("diary:diary_list")
