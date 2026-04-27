weekly_goal_minutes = 120

study_tasks = [
    {
        "course_name": "Python Programming",
        "task_name": "Finish decisions practice",
        "priority": "high",
        "completed": False,
        "estimated_minutes": 40,
    },
    {
        "course_name": "History 101",
        "task_name": "Read chapter summary",
        "priority": "medium",
        "completed": True,
        "estimated_minutes": 30,
    },
    {
        "course_name": "Biology",
        "task_name": "Review cell vocabulary",
        "priority": "low",
        "completed": True,
        "estimated_minutes": 55,
    },
]

total_planned_minutes = 0
total_completed_minutes = 0

print("StudyPilot - Week 2 Snapshot")
print()

for task in study_tasks:
    print("Course:", task["course_name"])
    print("Task:", task["task_name"])
    print("Priority:", task["priority"])
    print("Estimated Minutes:", task["estimated_minutes"])

    if task["priority"] == "high":
        print("Priority Check: Study this task soon.")
    else:
        print("Priority Check: This task can wait a little longer.")

    if task["completed"]:
        print("Completion Check: Task finished.")
        total_completed_minutes = total_completed_minutes + task["estimated_minutes"]
    else:
        print("Completion Check: Task still needs work.")

    total_planned_minutes = total_planned_minutes + task["estimated_minutes"]
    print()

remaining_minutes = total_planned_minutes - total_completed_minutes

print("Weekly Goal Minutes:", weekly_goal_minutes)
print("Planned Study Minutes:", total_planned_minutes)
print("Completed Study Minutes:", total_completed_minutes)
print("Remaining Planned Minutes:", remaining_minutes)

if total_completed_minutes >= weekly_goal_minutes:
    print("Weekly Goal Check: You met your weekly study goal.")
else:
    print("Weekly Goal Check: You have not met your weekly study goal yet.")
