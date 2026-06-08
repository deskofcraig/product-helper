# Task Update Prompt

Use this prompt to update the status of one or more tasks and trigger a plan re-evaluation.

---

## Prompt

You are acting as the personal assistant agent defined in `agent/system_prompt.md`.

The user has provided updates on task progress. Apply the updates to the task list and determine whether the plan needs to be adjusted.

**Current task list:**
```json
{{CURRENT_TASK_LIST_JSON}}
```

**User-provided updates:**
```
{{USER_UPDATES}}

Examples of valid update formats:
- "task-003 is done — took about 2 hours"
- "task-005 is delayed, waiting on legal sign-off, probably 3 more days"
- "task-007 is in progress, about 50% done"
- "task-009 is blocked by John, he hasn't sent the data yet"
- "Cancel task-011, no longer needed"
```

---

## Actions to Perform

1. **Parse the updates** — identify which tasks are being updated and what their new status is.

2. **Apply updates** — return the updated task JSON for each changed task.

3. **Check for unblocked tasks** — if a task was completed, check whether any tasks that depended on it are now unblocked and update their status to `pending`.

4. **Check for newly blocked tasks** — if a task is delayed or blocked, identify downstream tasks that are now affected and update their status.

5. **Flag deadline risks** — if any updates create a risk to a project deadline, say so clearly.

6. **Record actual time** — if the user provided how long a task took, record it for the learning store.

---

## Output Format

### Updated Tasks (JSON)

Return only the changed task objects:

```json
[
  {
    "id": "task-003",
    "status": "completed",
    "actual_minutes": 120,
    "completed_date": "{{TODAY}}"
  }
]
```

### Cascade Effects

List any tasks whose status changed as a result of this update (e.g. tasks that are now unblocked):

```
task-006: pending → now unblocked (task-003 completed)
task-007: pending → blocked (task-005 now delayed)
```

### Deadline Impact

```
[NO IMPACT] — All deadlines still on track.
```
or
```
[AT RISK] — task-005 delay pushes project-alpha completion to DD MMM (was DD MMM).
Recommend: [specific action]
```

### Learning Store Entry (if task completed)

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
