from django import forms

from .models import StudySession, StudyTask


class StudyTaskForm(forms.ModelForm):
    class Meta:
        model = StudyTask
        fields = [
            "course_name",
            "topic",
            "task_name",
            "priority",
            "due_date",
            "estimated_minutes",
        ]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }


class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = [
            "course_name",
            "topic",
            "minutes_studied",
            "session_date",
            "notes",
        ]
        widgets = {
            "session_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 4}),
        }
