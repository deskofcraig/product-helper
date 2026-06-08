# agenticHelpers

A personal AI assistant agent that sends you a daily structured briefing covering your work and personal tasks, meetings, priorities, and who to connect with — helping you stay on top of delivery, communication, and focus.

---

## What it does

- **Daily briefing** — calendar, email actions, task focus list, overdue items, people to contact, week snapshot
- **Task management** — reads, generates, and updates a to-do list
- **Project planning** — breaks down project descriptions into time-estimated, dependency-mapped task lists
- **Timeline estimation** — schedules tasks around your calendar; learns from actual vs estimated time to improve future estimates
- **Progress tracking** — accepts completed / in-progress / delayed updates and adjusts plans and timelines accordingly
- **People awareness** — uses coworker profiles to recommend who to involve and when
- **External agent integration** — can pull context from other agentic AI directories
- **Scheduled execution** — runs automatically via cron, launchd, Task Scheduler, or GitHub Actions

---

## AI-tool agnostic

Works with any major AI provider. Set your preferred provider in `config/config.yaml`:

| Provider | Model examples |
|---|---|
| Anthropic (Claude) | claude-sonnet-4-6, claude-opus-4-6 |
| OpenAI | gpt-4o, gpt-4-turbo |
| Google | gemini-1.5-pro |
| Azure OpenAI | Your deployed model name |
| Ollama (local) | llama3, mistral, phi3 |

---

## File structure

```
agenticHelpers/
├── README.md                          # This file
├── SETUP.md                           # Step-by-step setup guide
├── HOW-TO-USE.md                      # Day-to-day usage guide
├── .gitignore                         # Keeps personal data out of git
│
├── agent/
│   ├── system_prompt.md               # Core agent instructions
│   ├── daily_briefing_prompt.md       # Prompt template for daily briefing
│   └── tools_manifest.md             # Integration status and config reference
│
├── config/
│   ├── config.example.yaml            # Config template (copy to config.yaml)
│   ├── user_profile.example.yaml      # Profile template (copy to user_profile.yaml)
│   └── schedule.yaml                  # Scheduled task definitions
│
├── prompts/
│   ├── daily_briefing.md              # Daily briefing output template
│   ├── task_breakdown.md              # Project → task list prompt
│   ├── timeline_estimation.md         # Task scheduling prompt
│   ├── adjust_plan.md                 # Plan recalculation prompt
│   ├── task_update.md                 # Task status update prompt
│   └── weekly_review.md              # Weekly review prompt
│
├── schemas/
│   ├── task.schema.json               # Task data structure
│   ├── project.schema.json            # Project data structure
│   └── coworker_profile.schema.json   # Coworker profile structure
│
├── runner/
│   ├── runner.py                      # Main orchestration script
│   └── requirements.txt              # Python dependencies
│
└── data/
    ├── tasks/
    │   └── todo.json                  # Active task list (gitignored)
    ├── projects/
    │   └── project_template.md        # Template for new project files
    ├── profiles/
    │   └── coworker_template.yaml     # Template for coworker profiles
    ├── learning/
    │   └── time_estimates.json        # Time estimation learning store (gitignored)
    ├── output/                        # Generated briefings (gitignored)
    ├── logs/                          # Agent logs (gitignored)
    └── job_description.md             # Your role and responsibilities (gitignored)
```

---

## Quick start

```bash
# 1. Clone your repo
git clone https://github.com/YOUR_USERNAME/agenticHelpers.git
cd agenticHelpers

# 2. Install dependencies
pip install -r runner/requirements.txt

# 3. Configure
cp config/config.example.yaml config/config.yaml
cp config/user_profile.example.yaml config/user_profile.yaml
# Edit both files with your details

# 4. Add your AI API key
mkdir -p config/secrets
echo "ANTHROPIC_API_KEY=your-key-here" > config/secrets/.env

# 5. Test
python runner/runner.py --dry-run

# 6. Run
python runner/runner.py --task daily_briefing
```

Full setup instructions: **[SETUP.md](SETUP.md)**  
Day-to-day usage: **[HOW-TO-USE.md](HOW-TO-USE.md)**

---

## Changing behaviour

All behaviour is controlled by markdown prompt files in `prompts/` and `agent/`. Edit them directly to change what the agent does and how it formats output. No code changes needed.

To experiment safely, use a git branch:

```bash
git checkout -b tweak/briefing-format
# Edit prompts/daily_briefing.md
python runner/runner.py --task daily_briefing  # Test
git add . && git commit -m "New briefing format"
# Merge when happy
```

---

## Privacy

Your personal data (tasks, project files, job description, coworker profiles, email and calendar data) is stored locally and excluded from git via `.gitignore`. Only the agent structure, prompts, and config templates are committed to the repo.

API keys are stored in `config/secrets/.env` which is also gitignored.
