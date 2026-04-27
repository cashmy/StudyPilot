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


def get_recently_completed_tasks(tasks, today=None, days=ROLLING_SUMMARY_DAYS):
    today = today or date.today()
    start_date = today - timedelta(days=days - 1)
    completed_tasks = []

    for task in tasks:
        if not task.get("completed", False):
            continue

        completed_date = parse_iso_date(task.get("completed_date", ""))
        if completed_date is None:
            continue

        if start_date <= completed_date <= today:
            completed_tasks.append(task)

    return sort_tasks(completed_tasks)


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
    estimated_minutes = 0

    for task in tasks:
        estimated_minutes += safe_minutes(task.get("estimated_minutes", 0))

    return estimated_minutes


def build_progress_summary(tasks, sessions, today=None, days=ROLLING_SUMMARY_DAYS):
    today = today or date.today()
    incomplete_tasks = get_incomplete_tasks(tasks)
    due_soon_tasks = get_due_soon_tasks(tasks, today=today)
    overdue_tasks = get_overdue_tasks(tasks, today=today)
    recent_sessions = get_recent_sessions(sessions, today=today, days=days)
    recently_completed_tasks = get_recently_completed_tasks(
        tasks, today=today, days=days
    )

    return {
        "summary_days": days,
        "incomplete_task_count": len(incomplete_tasks),
        "due_soon_task_count": len(due_soon_tasks),
        "overdue_task_count": len(overdue_tasks),
        "recently_completed_task_count": len(recently_completed_tasks),
        "estimated_remaining_minutes": sum_estimated_minutes(incomplete_tasks),
        "recent_session_count": len(recent_sessions),
        "recent_minutes": total_minutes(recent_sessions),
        "recent_course_totals": minutes_by_course(recent_sessions),
        "recent_topic_totals": minutes_by_topic(recent_sessions),
        "all_time_minutes": total_minutes(sessions),
        "all_time_course_totals": minutes_by_course(sessions),
        "all_time_topic_totals": minutes_by_topic(sessions),
    }


def get_least_studied_course(tasks, sessions, today=None, days=ROLLING_SUMMARY_DAYS):
    courses = set()

    for task in get_incomplete_tasks(tasks):
        course_name = str(task.get("course_name", "")).strip()
        if course_name:
            courses.add(course_name)

    recent_course_totals = minutes_by_course(
        get_recent_sessions(sessions, today=today, days=days)
    )
    for course_name in recent_course_totals:
        courses.add(course_name)

    if len(courses) < 2:
        return ""

    lowest_course = ""
    lowest_minutes = None

    for course_name in sorted(courses):
        course_minutes = recent_course_totals.get(course_name, 0)
        if lowest_minutes is None or course_minutes < lowest_minutes:
            lowest_course = course_name
            lowest_minutes = course_minutes

    return lowest_course


def get_next_focus_task(tasks):
    incomplete_tasks = get_incomplete_tasks(tasks)
    if not incomplete_tasks:
        return None

    return incomplete_tasks[0]


def build_recommendations(tasks, sessions, today=None, days=ROLLING_SUMMARY_DAYS):
    summary = build_progress_summary(tasks, sessions, today=today, days=days)
    recommendations = []

    overdue_count = summary["overdue_task_count"]
    if overdue_count:
        task_label = "task" if overdue_count == 1 else "tasks"
        recommendations.append(
            f"You have {overdue_count} overdue {task_label}. Start with the oldest due task."
        )

    due_soon_count = summary["due_soon_task_count"]
    if due_soon_count:
        task_label = "task" if due_soon_count == 1 else "tasks"
        recommendations.append(
            f"Prioritize {due_soon_count} {task_label} due within {DUE_SOON_DAYS} days."
        )

    if summary["incomplete_task_count"] and summary["recent_minutes"] == 0:
        recommendations.append(
            f"You have open tasks but no study time logged in the last {days} days."
        )

    if (
        summary["estimated_remaining_minutes"] > summary["recent_minutes"]
        and summary["incomplete_task_count"]
    ):
        recommendations.append(
            f"Your estimated remaining work is higher than your logged study time in the last {days} days."
        )

    least_studied_course = get_least_studied_course(
        tasks, sessions, today=today, days=days
    )
    if least_studied_course:
        recommendations.append(
            f"{least_studied_course} has the fewest logged study minutes in the last {days} days."
        )

    if not recommendations:
        next_focus_task = get_next_focus_task(tasks)
        if next_focus_task is None:
            recommendations.append(
                "You have no open tasks right now. Add a new study task when you are ready."
            )
        else:
            recommendations.append(
                f"Your next focus could be {next_focus_task['course_name']}: {next_focus_task['task_name']}."
            )

    return recommendations
