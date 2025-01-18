from django.shortcuts import render
from django.views.generic import ListView

from diary.models import Diary


class DiaryListView(ListView):
    model = Diary

