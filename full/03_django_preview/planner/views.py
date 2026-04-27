from datetime import timedelta

from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import StudySessionForm, StudyTaskForm
from .models import StudySession, StudyTask


def dashboard(request):
    today = timezone.localdate()
    last_7_days = today - timedelta(days=6)

    tasks = StudyTask.objects.all()
    sessions = StudySession.objects.all()
    recent_sessions = sessions.filter(
        session_date__gte=last_7_days, session_date__lte=today
    )

    recent_minutes = (
        recent_sessions.aggregate(total=Sum("minutes_studied"))["total"] or 0
    )
    all_time_minutes = sessions.aggregate(total=Sum("minutes_studied"))["total"] or 0
    estimated_remaining_minutes = (
        tasks.filter(completed=False).aggregate(total=Sum("estimated_minutes"))["total"]
        or 0
    )

    context = {
        "task_count": tasks.count(),
        "open_task_count": tasks.filter(completed=False).count(),
        "completed_task_count": tasks.filter(completed=True).count(),
        "due_soon_tasks": [task for task in tasks if task.is_due_soon()],
        "overdue_tasks": [task for task in tasks if task.is_overdue()],
        "recent_session_count": recent_sessions.count(),
        "recent_minutes": recent_minutes,
        "all_time_minutes": all_time_minutes,
        "estimated_remaining_minutes": estimated_remaining_minutes,
        "recent_sessions": recent_sessions[:5],
    }
    return render(request, "planner/dashboard.html", context)


def task_list(request):
    tasks = StudyTask.objects.all()
    return render(request, "planner/task_list.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        form = StudyTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("planner:task_list")
    else:
        form = StudyTaskForm()

    return render(
        request,
        "planner/task_form.html",
        {
            "form": form,
            "page_title": "Add Study Task",
        },
    )


def complete_task(request, task_id):
    task = get_object_or_404(StudyTask, pk=task_id)

    if request.method == "POST" and not task.completed:
        task.mark_completed()

    return redirect("planner:task_list")


def add_session(request):
    if request.method == "POST":
        form = StudySessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("planner:session_list")
    else:
        form = StudySessionForm()

    return render(
        request,
        "planner/session_form.html",
        {
            "form": form,
            "page_title": "Log Study Session",
        },
    )


def session_list(request):
    sessions = StudySession.objects.all()
    total_minutes = sessions.aggregate(total=Sum("minutes_studied"))["total"] or 0

    return render(
        request,
        "planner/session_list.html",
        {
            "sessions": sessions,
            "total_minutes": total_minutes,
        },
    )
