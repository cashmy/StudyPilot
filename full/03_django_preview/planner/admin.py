from django.contrib import admin

from .models import StudySession, StudyTask


@admin.register(StudyTask)
class StudyTaskAdmin(admin.ModelAdmin):
    list_display = ("task_name", "course_name", "priority", "due_date", "completed")
    list_filter = ("completed", "priority", "course_name")
    search_fields = ("task_name", "course_name", "topic")


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ("course_name", "topic", "minutes_studied", "session_date")
    list_filter = ("course_name", "session_date")
    search_fields = ("course_name", "topic", "notes")
