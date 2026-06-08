# Plan Adjustment Prompt

Use this prompt when task progress has been updated and the plan needs to be recalculated.

---

## Prompt

You are acting as the personal assistant agent defined in `agent/system_prompt.md`.

Task progress has been updated. Review the current task list and recalculate the plan, timeline, and priorities based on the new state.

**Updated task list:**
```json
{{UPDATED_TASK_LIST_JSON}}
```

**Changes since last plan:**
```
{{CHANGES_SUMMARY}}
(e.g. "task-003 marked delayed by 2 days due to waiting on legal review",
      "task-005 completed — actual time: 90 min vs estimated 60 min",
      "task-007 blocked — waiting on design sign-off from Sarah")
```

**Current date:** {{TODAY}}
**Original target completion:** {{ORIGINAL_TARGET_DATE}}

**Calendar for the remaining period:**
```
{{CALENDAR_EVENTS}}
```

---

## Output Format

### Impact Assessment

For each changed task, state:
- What changed
- Which downstream tasks are affected
- Whether the target completion date is still achievable

Format:
```
TASK task-003 [DELAYED +2 days]
→ Affects: task-006, task-008 (both blocked by task-003)
→ New earliest start for task-006: DD MMM
→ Impact on target date: TARGET DATE NOW AT RISK — slips by 2 days
```

### Updated Timeline

Produce a revised schedule using the same format as `prompts/timeline_estimation.md`.

Focus on:
- Reprioritised task order given the new state
- Rescheduled tasks that were unblocked or re-blocked
- Any tasks that should be cut, deferred, or de-scoped to protect the deadline

### Recommendations

1. **Immediate actions** — What should the user do right now to mitigate the impact?
2. **Escalate** — Should anyone be informed of the delay? (Reference coworker profiles in `data/profiles/`)
3. **De-scope options** — If the deadline is at risk, what could be cut with minimal impact?
4. **New estimates** — If any tasks have completed faster or slower than expected, note the learning and confirm the learning store should be updated.

### Learning Store Updates

For any completed tasks, output the update to add to `data/learning/time_estimates.json`:

```json
{
  "task_category": "{{CATEGORY}}",
  "new_data_point": {
    "estimated_minutes": {{ESTIMATED}},
    "actual_minutes": {{ACTUAL}},
    "date": "{{TODAY}}"
  }
}
```
