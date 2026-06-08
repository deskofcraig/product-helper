# How to Use agenticHelpers

This guide covers day-to-day usage of the agent once it's set up.

---

## Running the Agent

### Get your daily briefing

```bash
python runner/runner.py --task daily_briefing
```

This generates a structured briefing covering your calendar, email actions, task focus list, overdue items, who to work with, and a week-ahead snapshot.

### Run the weekly review (every Friday)

```bash
python runner/runner.py --task weekly_review
```

Generates a review of the week — what was completed, what carried over, what was missed — and a forward plan for next week.

### Break down a project into tasks

```bash
python runner/runner.py --task task_breakdown --project data/projects/my_project.md
```

The agent reads your project description and generates a full, time-estimated, dependency-mapped task list. The output is printed and saved to `data/output/`.

### Update task progress

```bash
python runner/runner.py --task update_tasks --updates "task-003 is done, took about 90 minutes. task-005 is delayed, waiting on legal review."
```

Or omit `--updates` to be prompted interactively:

```bash
python runner/runner.py --task update_tasks
```

The agent applies the updates, cascades any status changes to dependent tasks, flags deadline risks, and records the actual time to the learning store.

---

## Adding Tasks Manually

Edit `data/tasks/todo.json` directly. Use `schemas/task.schema.json` as a reference for valid fields. At minimum, each task needs:

```json
{
  "id": "task-unique-id",
  "title": "Do the thing",
  "status": "pending",
  "priority": "high",
  "created_date": "2026-06-02"
}
```

---

## Adding a Project

1. Copy the template: `cp data/projects/project_template.md data/projects/my-project.md`
2. Fill it in — name, description, success criteria, milestones, stakeholders
3. Run the task breakdown to generate tasks from it

---

## Adding a Coworker Profile

1. Copy the template: `cp data/profiles/coworker_template.yaml data/profiles/firstname_lastname.yaml`
2. Fill in their role, expertise, how they like to work, and when to involve them
3. The agent will reference their profile in daily briefings and task recommendations

---

## Changing Agent Behaviour

The agent's behaviour is controlled by plain text files. You can change how it works without touching any code.

### Change the daily briefing format

Edit `prompts/daily_briefing.md`. For example:
- Remove the "Week Ahead Snapshot" section if you don't want it
- Add a new section for "Personal tasks"
- Change the focus recommendation to be more brief

### Change estimation style

Edit `prompts/timeline_estimation.md`. For example:
- Adjust the buffer percentage for low-confidence estimates
- Change the minimum gap between tasks
- Add your own estimation rules

### Change what the agent prioritises

Edit `agent/system_prompt.md` → "Behaviour Rules" section. For example:
- "Always surface stakeholder communication tasks in the top 3"
- "Never schedule deep work on days with more than 3 hours of meetings"

### Making changes on a branch (safe experimentation)

```bash
git checkout -b experiment/new-briefing-format
# Edit prompts/daily_briefing.md
python runner/runner.py --task daily_briefing  # Test it
# If happy:
git add prompts/daily_briefing.md
git commit -m "Adjust daily briefing format"
git checkout main
git merge experiment/new-briefing-format
```

---

## Updating Task Status

Task statuses you can use:

| Status | When to use |
|---|---|
| `pending` | Not started yet |
| `in_progress` | Currently being worked on |
| `completed` | Done |
| `delayed` | Started but behind schedule |
| `blocked` | Cannot proceed — waiting on something external |
| `cancelled` | No longer needed |

Update via the runner:
```bash
python runner/runner.py --task update_tasks --updates "task-007 is blocked, waiting on design sign-off"
```

Or edit `data/tasks/todo.json` directly.

---

## Understanding the Learning Store

The file `data/learning/time_estimates.json` records how long tasks actually took vs how long the agent estimated. Over time this makes future estimates more accurate.

You don't need to manage this file manually — the agent updates it automatically when you mark tasks complete and provide the actual time. After about 10–15 data points per task category, estimates become reliable.

To reset the learning store (e.g. if your role changes significantly):

```bash
echo '{"_readme": "Reset on YYYY-MM-DD", "categories": {}}' > data/learning/time_estimates.json
```

---

## Connecting to External Agent Directories

If you have other AI agent directories (e.g. a project-specific agent, a code assistant), you can point this agent at them to pull in context:

1. In `config/config.yaml`, set `external_agents.enabled: true`
2. Add the path to the other agent's directory
3. Specify which files to read (e.g. `tasks.json`, `README.md`, `context.md`)

The agent will include that content in its briefings and task planning.

---

## Output Files

All agent outputs are saved to `data/output/` with a timestamp in the filename:
```
data/output/daily_briefing_20260602_073012.md
data/output/weekly_review_20260530_160000.md
data/output/task_breakdown_20260601_094512.md
```

These files are in `.gitignore` and won't be committed.

---

## Adjusting the Schedule

Open `config/schedule.yaml` to see and adjust when the agent runs automatically. Schedules use standard cron syntax.

```yaml
daily_briefing:
  enabled: true
  cron: "30 7 * * 1-5"   # 07:30 Mon–Fri
```

See `SETUP.md → Step 10` for instructions on registering the schedule with your OS.

---

## Switching AI Providers

The agent is AI-tool agnostic. To switch providers:

1. Open `config/config.yaml`
2. Change `ai.provider` and `ai.model`
3. Add the new provider's API key to `config/secrets/.env`
4. Install the new provider's package (see `runner/requirements.txt`)

No other changes needed — the runner handles the rest.

---

## Tips

- **Keep project files up to date.** The better the project descriptions, the better the task breakdowns.
- **Be specific when updating tasks.** "task-003 done, took 2 hours" gives the agent better data than just "done".
- **Use the weekly review.** It takes 2 minutes to scan and helps you course-correct before deadlines creep up.
- **Add coworker profiles for the people you work with most.** Even a minimal profile (role + expertise + when to involve them) meaningfully improves recommendations.
- **Branch before experimenting.** If you want to try a different briefing format or prompt style, do it on a branch so you can roll back if needed.
