
from django.urls import path, include


from diary.apps import DiaryConfig
from diary.views import DiaryListView, DiaryCreateView, DiaryUpdateView, DiaryDetailView, DiaryDeleteView

app_name = DiaryConfig.name

urlpatterns = [
    path("", DiaryListView.as_view(), name="diary_list"),
    path("create/", DiaryCreateView.as_view(), name="diary_create"),
    path("update/<int:pk>/", DiaryUpdateView.as_view(), name="diary_update"),
    path("detail/<int:pk>", DiaryDetailView.as_view(), name="diary_detail"),
    path("delete/<int:pk>/", DiaryDeleteView.as_view(), name="diary_delete"),
]
