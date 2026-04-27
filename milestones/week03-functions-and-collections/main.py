def add_task(task_list, course_name, task_name, priority, completed, estimated_minutes):
    task = {
        "course_name": course_name,
        "task_name": task_name,
        "priority": priority,
        "completed": completed,
        "estimated_minutes": estimated_minutes,
    }
    task_list.append(task)
    return task


def display_task(task):
    print("Course:", task["course_name"])
    print("Task:", task["task_name"])
    print("Priority:", task["priority"])
    print("Estimated Minutes:", task["estimated_minutes"])


def evaluate_task(task):
    if task["priority"] == "high":
        priority_message = "Study this task soon."
    else:
        priority_message = "This task can wait a little longer."

    if task["completed"]:
        completion_message = "Task finished."
        completed_minutes = task["estimated_minutes"]
    else:
        completion_message = "Task still needs work."
        completed_minutes = 0

    return {
        "priority_message": priority_message,
        "completion_message": completion_message,
        "completed_minutes": completed_minutes,
    }


def summarize_tasks(task_list, weekly_goal_minutes):
    total_planned_minutes = 0
    total_completed_minutes = 0

    for task in task_list:
        total_planned_minutes = total_planned_minutes + task["estimated_minutes"]

        if task["completed"]:
            total_completed_minutes = (
                total_completed_minutes + task["estimated_minutes"]
            )

    remaining_planned_minutes = total_planned_minutes - total_completed_minutes
    goal_met = total_completed_minutes >= weekly_goal_minutes

    return {
        "total_planned_minutes": total_planned_minutes,
        "total_completed_minutes": total_completed_minutes,
        "remaining_planned_minutes": remaining_planned_minutes,
        "goal_met": goal_met,
    }


weekly_goal_minutes = 120
study_tasks = []

add_task(
    study_tasks,
    "Python Programming",
    "Finish decisions practice",
    "high",
    False,
    40,
)
add_task(
    study_tasks,
    "History 101",
    "Read chapter summary",
    "medium",
    True,
    30,
)
add_task(
    study_tasks,
    "Biology",
    "Review cell vocabulary",
    "low",
    True,
    55,
)

print("StudyPilot - Week 3 Snapshot")
print()

for task in study_tasks:
    display_task(task)
    task_evaluation = evaluate_task(task)
    print("Priority Check:", task_evaluation["priority_message"])
    print("Completion Check:", task_evaluation["completion_message"])
    print()

study_summary = summarize_tasks(study_tasks, weekly_goal_minutes)

print("Weekly Goal Minutes:", weekly_goal_minutes)
print("Planned Study Minutes:", study_summary["total_planned_minutes"])
print("Completed Study Minutes:", study_summary["total_completed_minutes"])
print("Remaining Planned Minutes:", study_summary["remaining_planned_minutes"])

if study_summary["goal_met"]:
    print("Weekly Goal Check: You met your weekly study goal.")
else:
    print("Weekly Goal Check: You have not met your weekly study goal yet.")
