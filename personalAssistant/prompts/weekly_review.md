# Weekly Review Prompt

Use this prompt each Friday (or end of working week) to review the week and plan the next.

---

## Prompt

You are acting as the personal assistant agent defined in `agent/system_prompt.md`.

The working week is ending. Generate a weekly review and forward plan.

**Week:** {{WEEK_START_DATE}} to {{WEEK_END_DATE}}

**Task list (current state):**
```json
{{TASK_LIST_JSON}}
```

**Calendar events this week:**
```
{{THIS_WEEK_CALENDAR}}
```

**Calendar events next week:**
```
{{NEXT_WEEK_CALENDAR}}
```

**Learning store (for estimation reference):**
```json
{{TIME_ESTIMATES_JSON}}
```

---

## Output Format

---

### 📊 Week in Review — {{WEEK_START_DATE}} to {{WEEK_END_DATE}}

#### ✅ Completed This Week
List all tasks completed this week. Include estimated vs actual time where available.

| Task | Project | Est. Time | Actual Time | Variance |
|---|---|---|---|---|
| Task name | Project | 60 min | 75 min | +15 min |

**Summary:** [X] tasks completed. [Total actual hours] worked on tasks.

---

#### 🟡 In Progress / Carried Over
List tasks that started but weren't completed.

| Task | Project | Status | Est. Remaining | Why not complete |
|---|---|---|---|---|

---

#### ❌ Missed / Overdue
List tasks that were due this week but not completed.

| Task | Project | Original Due Date | New Due Date | Impact |
|---|---|---|---|---|

---

#### 🧠 What We Learned This Week
Based on actual vs estimated times, note any patterns:
- Tasks that consistently take longer than estimated
- Categories where estimates are improving
- Suggestions for how to adjust future estimates

---

### 📅 Next Week Plan

#### Calendar Overview
List next week's meetings and events grouped by day. Flag any prep needed.

#### Task Focus List
Top tasks to complete next week, ordered by priority and accounting for calendar load.

| Priority | Task | Project | Estimated Time | Target Day |
|---|---|---|---|---|
| 1 | | | | |

#### Time Available for Task Work
After accounting for meetings, how many hours are available for focused task work each day?

| Day | Meeting Hours | Available Hours | Notes |
|---|---|---|---|
| Monday | | | |

#### Deadlines Next Week
Any tasks or project milestones due next week.

#### Who to Work With Next Week
Based on tasks and calendar, list the people to connect with and why.

---

### 🔭 2-Week Outlook
Brief summary of the week after next — any big deadlines, milestones, or focus areas to be aware of now.

---

### 📝 Recommendations
3–5 specific recommendations for next week based on the review. Be direct and actionable.
