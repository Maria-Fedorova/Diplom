from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from diary.forms import DiaryForm
from diary.models import Diary


class DiaryListView(ListView):
    model = Diary
    form_class = DiaryForm

    def get_queryset(self):
        return Diary.objects.filter(author=self.request.user)


class DiaryCreateView(CreateView):
    model = Diary
    form_class = DiaryForm
    success_url = reverse_lazy("diary:diary_list")


class DiaryUpdateView(UpdateView):
    model = Diary
    success_url = reverse_lazy("diary:diary_list")


class DiaryDetailView(DetailView):
    model = Diary


class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:diary_list')
