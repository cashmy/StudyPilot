from main import build_sample_tasks, summarize_tasks_buggy, summarize_tasks_fixed


def test_buggy_summary_does_not_match_expected_completed_minutes():
    study_tasks = build_sample_tasks()
    summary = summarize_tasks_buggy(study_tasks, 120)

    assert summary["total_completed_minutes"] != 85


def test_fixed_summary_matches_expected_values():
    study_tasks = build_sample_tasks()
    summary = summarize_tasks_fixed(study_tasks, 120)

    assert summary["total_planned_minutes"] == 125
    assert summary["total_completed_minutes"] == 85
    assert summary["remaining_planned_minutes"] == 40
    assert summary["goal_met"] is False
