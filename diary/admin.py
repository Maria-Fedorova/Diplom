from django.contrib import admin

from diary.models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "create_date",
        "updated_date",
        "author",
    )
    list_filter = ("author", "title", "create_date", "updated_date")
    search_fields = (
        "author",
        "title",
    )
