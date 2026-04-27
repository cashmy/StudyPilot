from django.urls import path

from . import views


app_name = "planner"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/<int:task_id>/complete/", views.complete_task, name="complete_task"),
    path("sessions/", views.session_list, name="session_list"),
    path("sessions/add/", views.add_session, name="add_session"),
]
