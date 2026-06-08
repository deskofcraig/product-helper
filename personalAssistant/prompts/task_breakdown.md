# Task Breakdown Prompt

Use this prompt to break a project or piece of work into a structured, time-estimated task list.

---

## Prompt

You are acting as the personal assistant agent defined in `agent/system_prompt.md`.

A project or piece of work has been provided below. Break it down into a clear, structured task list. Each task should be:
- Specific and actionable
- Small enough to be completed in a single focused session (ideally under 2 hours)
- Time-estimated based on historical data in `data/learning/time_estimates.json` (if available) or reasonable professional estimates
- Ordered logically with dependencies identified

**Project/Work context:**
```
{{PROJECT_OR_WORK_DESCRIPTION}}
```

**Constraints:**
- Start date: {{START_DATE}}
- Target completion date: {{TARGET_DATE}}
- Working hours per day available: {{HOURS_PER_DAY}}
- Key stakeholders: {{STAKEHOLDERS}}
- Known dependencies or blockers: {{KNOWN_DEPENDENCIES}}

---

## Output Format

Return the task list as a JSON array conforming to `schemas/task.schema.json`, followed by a plain-English summary.

### JSON Task List

```json
[
  {
    "id": "task-001",
    "title": "Task title",
    "description": "What needs to be done and what done looks like",
    "status": "pending",
    "priority": "high",
    "category": "work",
    "project_id": "{{PROJECT_ID}}",
    "estimated_minutes": 60,
    "due_date": "YYYY-MM-DD",
    "created_date": "{{TODAY}}",
    "depends_on": [],
    "blocks": ["task-002"],
    "tags": [],
    "source": "agent_generated"
  }
]
```

### Plain-English Summary

After the JSON, write a short summary covering:
1. **Total estimated time** across all tasks
2. **Critical path** — the sequence of tasks that determines the earliest completion date
3. **Key risks** — tasks most likely to take longer than estimated or to cause delays
4. **Suggested start order** — the first 3 tasks to begin
5. **Timeline fit** — whether the work fits within the target date given available hours, and if not, what to cut or defer

---

## Dependency Rules

When identifying dependencies, apply these rules:
- If Task B requires the output of Task A, Task A must be in `depends_on` for Task B
- If tasks can be done in parallel, do not create unnecessary dependencies
- Flag any external dependencies (waiting on another person) clearly in the task description and tags
- Mark tasks with external dependencies as `"status": "blocked"` if the blocker is known at time of generation
