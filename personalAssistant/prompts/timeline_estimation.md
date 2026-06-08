# Timeline Estimation Prompt

Use this prompt to estimate timelines for a task list and produce a schedule.

---

## Prompt

You are acting as the personal assistant agent defined in `agent/system_prompt.md`.

Given the task list below, produce a realistic timeline and schedule. Account for the user's working hours, existing calendar commitments, and historical time estimates from `data/learning/time_estimates.json`.

**Task list:**
```json
{{TASK_LIST_JSON}}
```

**Calendar commitments for the period:**
```
{{CALENDAR_EVENTS}}
```

**Working constraints:**
- Working hours: {{WORKING_HOURS_START}} to {{WORKING_HOURS_END}}
- Working days: {{WORKING_DAYS}}
- Deep work preference: {{DEEP_WORK_PREFERENCE}} (morning/afternoon/none)
- Planning period: {{START_DATE}} to {{END_DATE}}

**Historical time estimates (from learning store):**
```json
{{TIME_ESTIMATES_JSON}}
```

---

## Output Format

### Timeline Table

| Task ID | Task | Estimated Time | Suggested Date | Suggested Time | Dependencies | Notes |
|---|---|---|---|---|---|---|
| task-001 | Task title | 60 min | YYYY-MM-DD | HH:MM–HH:MM | None | |

### Gantt-Style Text View

```
[Week of DD MMM]
Mon: [task-001 60m] [task-002 90m] -- MEETING: Team standup 09:00
Tue: [task-003 120m (deep work)] [task-004 30m]
Wed: ...
```

### Key Dates

- **Earliest possible completion:** [date]
- **Recommended completion target:** [date] (includes buffer)
- **Buffer included:** [X days / X hours]

### Estimation Confidence

For each task, note the confidence in the estimate:
- **High** — Based on ≥3 historical data points
- **Medium** — Based on 1–2 data points or similar tasks
- **Low** — No historical data, using professional estimate

### Risk Flags

List any timeline risks:
- Tasks where the estimate has high variance in historical data
- Tasks on the critical path with Low confidence estimates
- Calendar days with high meeting load that compress available work time
- Any task that, if delayed by 1 day, would push the final deadline

---

## Estimation Rules

1. Never schedule deep work tasks into meeting-heavy days without explicit confirmation.
2. Add a 20% time buffer to tasks with Low confidence estimates.
3. Do not schedule tasks back-to-back without at least 15 minutes between them.
4. Respect the user's deep work preference (morning or afternoon blocks).
5. External-dependency tasks should be scheduled conservatively — assume the dependency arrives 1 day later than expected.
6. Tasks marked `blocked` should not be scheduled until the block is resolved.
