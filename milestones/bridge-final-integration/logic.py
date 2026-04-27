from datetime import date, timedelta


DUE_SOON_DAYS = 2
ROLLING_SUMMARY_DAYS = 7
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def parse_iso_date(date_text):
    if not date_text:
        return None

    try:
        return date.fromisoformat(date_text)
    except ValueError:
        return None


def safe_minutes(value):
    if isinstance(value, int):
        return max(0, value)

    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return 0


def task_sort_key(task):
    due_date = parse_iso_date(task.get("due_date", ""))
    priority = str(task.get("priority", "")).lower()

    return (
        task.get("completed", False),
        due_date is None,
        due_date or date.max,
        PRIORITY_ORDER.get(priority, 3),
        str(task.get("course_name", "")).lower(),
        str(task.get("task_name", "")).lower(),
    )


def sort_tasks(tasks):
    return sorted(tasks, key=task_sort_key)


def sort_sessions(sessions):
    return sorted(
        sessions,
        key=lambda session: (
            parse_iso_date(session.get("session_date", "")) or date.min,
            str(session.get("course_name", "")).lower(),
            str(session.get("topic", "")).lower(),
        ),
        reverse=True,
    )


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task.get("id") == task_id:
            return task

    return None


def get_incomplete_tasks(tasks):
    return [task for task in sort_tasks(tasks) if not task.get("completed", False)]


def get_due_soon_tasks(tasks, today=None, days=DUE_SOON_DAYS):
    today = today or date.today()
    due_soon_tasks = []

    for task in tasks:
        if task.get("completed", False):
            continue

        due_date = parse_iso_date(task.get("due_date", ""))
        if due_date is None:
            continue

        days_until_due = (due_date - today).days
        if 0 <= days_until_due <= days:
            due_soon_tasks.append(task)

    return sort_tasks(due_soon_tasks)


def get_overdue_tasks(tasks, today=None):
    today = today or date.today()
    overdue_tasks = []

    for task in tasks:
        if task.get("completed", False):
            continue

        due_date = parse_iso_date(task.get("due_date", ""))
        if due_date is not None and due_date < today:
            overdue_tasks.append(task)

    return sort_tasks(overdue_tasks)


def get_recent_sessions(sessions, today=None, days=ROLLING_SUMMARY_DAYS):
    today = today or date.today()
    start_date = today - timedelta(days=days - 1)
    recent_sessions = []

    for session in sessions:
        session_date = parse_iso_date(session.get("session_date", ""))
        if session_date is None:
            continue

        if start_date <= session_date <= today:
            recent_sessions.append(session)

    return sort_sessions(recent_sessions)


def total_minutes(sessions):
    minutes = 0

    for session in sessions:
        minutes += safe_minutes(session.get("minutes_studied", 0))

    return minutes


def totals_by_field(sessions, field_name):
    totals = {}

    for session in sessions:
        label = str(session.get(field_name, "")).strip() or f"Unknown {field_name}"
        totals[label] = totals.get(label, 0) + safe_minutes(
            session.get("minutes_studied", 0)
        )

    return dict(sorted(totals.items(), key=lambda item: (-item[1], item[0].lower())))


def minutes_by_course(sessions):
    return totals_by_field(sessions, "course_name")


def minutes_by_topic(sessions):
    return totals_by_field(sessions, "topic")


def sum_estimated_minutes(tasks):
    minutes = 0

    for task in tasks:
        minutes += safe_minutes(task.get("estimated_minutes", 0))

    return minutes


def build_progress_summary(tasks, sessions, today=None, days=ROLLING_SUMMARY_DAYS):
    today = today or date.today()
    incomplete_tasks = get_incomplete_tasks(tasks)
    due_soon_tasks = get_due_soon_tasks(tasks, today=today)
    overdue_tasks = get_overdue_tasks(tasks, today=today)
    recent_sessions = get_recent_sessions(sessions, today=today, days=days)

    return {
        "summary_days": days,
        "incomplete_task_count": len(incomplete_tasks),
        "due_soon_task_count": len(due_soon_tasks),
        "overdue_task_count": len(overdue_tasks),
        "estimated_remaining_minutes": sum_estimated_minutes(incomplete_tasks),
        "recent_session_count": len(recent_sessions),
        "recent_minutes": total_minutes(recent_sessions),
        "recent_course_totals": minutes_by_course(recent_sessions),
        "recent_topic_totals": minutes_by_topic(recent_sessions),
        "all_time_minutes": total_minutes(sessions),
        "all_time_course_totals": minutes_by_course(sessions),
        "all_time_topic_totals": minutes_by_topic(sessions),
    }


def build_recommendations(tasks, sessions):
    summary = build_progress_summary(tasks, sessions)
    recommendations = []

    if summary["overdue_task_count"]:
        recommendations.append(
            f"You have {summary['overdue_task_count']} overdue task(s). Start with the oldest due task."
        )

    if summary["due_soon_task_count"]:
        recommendations.append(f"Prioritize tasks due within {DUE_SOON_DAYS} days.")

    if summary["incomplete_task_count"] and summary["recent_minutes"] == 0:
        recommendations.append(
            f"You have open tasks but no study time logged in the last {ROLLING_SUMMARY_DAYS} days."
        )

    if (
        summary["estimated_remaining_minutes"] > summary["recent_minutes"]
        and summary["incomplete_task_count"]
    ):
        recommendations.append(
            "Estimated remaining work is higher than your recent logged study time."
        )

    if not recommendations:
        recommendations.append(
            "You have a workable balance right now. Keep logging study sessions and updating tasks."
        )

    return recommendations
