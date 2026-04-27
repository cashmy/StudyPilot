from datetime import timedelta

from django.db import models
from django.utils import timezone


class StudyTask(models.Model):
    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    course_name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    task_name = models.CharField(max_length=150)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="medium"
    )
    due_date = models.DateField(blank=True, null=True)
    estimated_minutes = models.PositiveIntegerField()
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["completed", "due_date", "course_name", "task_name"]

    def __str__(self):
        return f"{self.course_name}: {self.task_name}"

    def is_overdue(self):
        if self.completed or self.due_date is None:
            return False

        return self.due_date < timezone.localdate()

    def is_due_soon(self):
        if self.completed or self.due_date is None:
            return False

        today = timezone.localdate()
        return today <= self.due_date <= today + timedelta(days=2)

    def mark_completed(self):
        self.completed = True
        self.completed_date = timezone.localdate()
        self.save(update_fields=["completed", "completed_date"])


class StudySession(models.Model):
    course_name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    minutes_studied = models.PositiveIntegerField()
    session_date = models.DateField(default=timezone.localdate)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-session_date", "course_name", "topic"]

    def __str__(self):
        return f"{self.course_name}: {self.minutes_studied} min on {self.session_date}"
