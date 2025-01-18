from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from diary.apps import DiaryConfig
from diary.views import DiaryListView

app_name = DiaryConfig.name

urlpatterns = [
    path("", DiaryListView.as_view(), name="diary_list"),
]
