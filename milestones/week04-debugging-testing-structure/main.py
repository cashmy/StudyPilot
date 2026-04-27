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


def build_sample_tasks():
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

    return study_tasks


def display_tasks(task_list):
    for task in task_list:
        print("Course:", task["course_name"])
        print("Task:", task["task_name"])
        print("Priority:", task["priority"])
        print("Completed:", task["completed"])
        print("Estimated Minutes:", task["estimated_minutes"])
        print()


def summarize_tasks_buggy(task_list, weekly_goal_minutes):
    total_planned_minutes = 0
    total_completed_minutes = 0

    for task in task_list:
        total_planned_minutes = total_planned_minutes + task["estimated_minutes"]
        total_completed_minutes = total_completed_minutes + task["estimated_minutes"]

    remaining_planned_minutes = total_planned_minutes - total_completed_minutes
    goal_met = total_completed_minutes >= weekly_goal_minutes

    return {
        "total_planned_minutes": total_planned_minutes,
        "total_completed_minutes": total_completed_minutes,
        "remaining_planned_minutes": remaining_planned_minutes,
        "goal_met": goal_met,
    }


def summarize_tasks_fixed(task_list, weekly_goal_minutes):
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


def print_check_result(label, expected_value, actual_value):
    if expected_value == actual_value:
        print(label + ": PASS")
    else:
        print(label + ": FAIL")
        print("Expected:", expected_value)
        print("Actual:", actual_value)


def print_debug_steps(task_list):
    print("Print-Debugging Walkthrough")
    print()

    for task in task_list:
        print("Checking task:", task["task_name"])
        print("completed =", task["completed"])
        print("estimated_minutes =", task["estimated_minutes"])

        if task["completed"]:
            print("This task should add to completed minutes.")
        else:
            print("This task should not add to completed minutes.")

        print()


def print_summary(label, summary):
    print(label)
    print("Planned Study Minutes:", summary["total_planned_minutes"])
    print("Completed Study Minutes:", summary["total_completed_minutes"])
    print("Remaining Planned Minutes:", summary["remaining_planned_minutes"])

    if summary["goal_met"]:
        print("Weekly Goal Check: You met your weekly study goal.")
    else:
        print("Weekly Goal Check: You have not met your weekly study goal yet.")

    print()


def main():
    weekly_goal_minutes = 120
    expected_completed_minutes = 85
    expected_remaining_minutes = 40

    study_tasks = build_sample_tasks()

    print("StudyPilot - Week 4 Snapshot")
    print()
    display_tasks(study_tasks)

    print("Expected-Versus-Actual Check With Buggy Summary")
    print()
    buggy_summary = summarize_tasks_buggy(study_tasks, weekly_goal_minutes)
    print_summary("Buggy Summary Output", buggy_summary)
    print_check_result(
        "Completed minutes should count only finished tasks",
        expected_completed_minutes,
        buggy_summary["total_completed_minutes"],
    )
    print_check_result(
        "Remaining minutes should be planned minus completed",
        expected_remaining_minutes,
        buggy_summary["remaining_planned_minutes"],
    )
    print()

    print_debug_steps(study_tasks)

    print("Corrected Summary After Debugging")
    print()
    fixed_summary = summarize_tasks_fixed(study_tasks, weekly_goal_minutes)
    print_summary("Fixed Summary Output", fixed_summary)
    print_check_result(
        "Completed minutes should count only finished tasks",
        expected_completed_minutes,
        fixed_summary["total_completed_minutes"],
    )
    print_check_result(
        "Remaining minutes should be planned minus completed",
        expected_remaining_minutes,
        fixed_summary["remaining_planned_minutes"],
    )


if __name__ == "__main__":
    main()
