# Setup Guide

This guide walks you through setting up the agenticHelpers personal assistant agent from scratch.

---

## Prerequisites

- Python 3.10 or higher
- A GitHub account (to host the repo)
- An API key for at least one AI provider (Claude, GPT-4, Gemini, or a local model via Ollama)

---

## Step 1 — Clone the repo

Create a new repo named `agenticHelpers` on your personal GitHub, then clone it:

```bash
git clone https://github.com/YOUR_USERNAME/agenticHelpers.git
cd agenticHelpers
```

---

## Step 2 — Install Python dependencies

```bash
pip install -r runner/requirements.txt
```

Then open `runner/requirements.txt` and uncomment the packages for the AI provider(s) and integrations you want. Install them:

```bash
pip install -r runner/requirements.txt
```

---

## Step 3 — Configure the agent

Copy the example config files:

```bash
cp config/config.example.yaml config/config.yaml
cp config/user_profile.example.yaml config/user_profile.yaml
```

Open each file and fill in your details. Key things to set:

- `config/config.yaml` → `user` section (name, email, timezone, working hours)
- `config/config.yaml` → `ai` section (provider, model)
- `config/user_profile.yaml` → your role, preferences, and focus areas

---

## Step 4 — Set up your AI provider credentials

Create the secrets file:

```bash
mkdir -p config/secrets
touch config/secrets/.env
```

Add your API key to `config/secrets/.env`:

```bash
# For Claude (Anthropic)
ANTHROPIC_API_KEY=your-key-here

# For OpenAI
# OPENAI_API_KEY=your-key-here

# For Google Gemini
# GOOGLE_API_KEY=your-key-here

# For Azure OpenAI
# AZURE_OPENAI_API_KEY=your-key-here
# AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
# AZURE_OPENAI_API_VERSION=2024-02-01
```

This file is in `.gitignore` — it will never be committed.

---

## Step 5 — Fill in your personal data files

### Job description

Edit `data/job_description.md` to describe your role, responsibilities, and what success looks like. This helps the agent prioritise correctly.

### Coworker profiles

For each key coworker, copy `data/profiles/coworker_template.yaml` and fill it in:

```bash
cp data/profiles/coworker_template.yaml data/profiles/jane_smith.yaml
```

You only need to add people who matter to your work — don't add everyone.

### Projects

For each active project, copy `data/projects/project_template.md`:

```bash
cp data/projects/project_template.md data/projects/my_project.md
```

---

## Step 6 — Test the setup

Run a dry run to check everything is configured correctly:

```bash
python runner/runner.py --dry-run
```

You should see:
```
Config loaded: provider=anthropic, model=claude-sonnet-4-6
Todo tasks: 1
Profiles: 0
Projects: 0
Dry run complete — all config and data files read successfully.
```

---

## Step 7 — Connect Calendar (optional but recommended)

### Google Calendar

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a project → Enable the **Google Calendar API**
3. Create credentials → OAuth 2.0 Client ID → Desktop app
4. Download the credentials JSON and save it to `config/secrets/google_credentials.json`
5. Install the package: `pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib`
6. In `config/config.yaml`, set `calendar.enabled: true` and `calendar.provider: google`
7. On first run, a browser window will open for you to authenticate

### Microsoft Outlook / Teams Calendar

1. Register an app in [Azure Active Directory](https://portal.azure.com)
2. Grant `Calendars.Read` permission
3. Save the client ID, secret, and tenant ID to `config/secrets/.env`:
   ```
   MS_CLIENT_ID=...
   MS_CLIENT_SECRET=...
   MS_TENANT_ID=...
   ```
4. Install: `pip install O365`
5. Set `calendar.provider: microsoft` in `config/config.yaml`

### iCal (read-only, simplest option)

1. Get the `.ics` URL from your calendar app (Google Calendar, Outlook, Apple Calendar all support this)
2. Set in `config/config.yaml`:
   ```yaml
   calendar:
     enabled: true
     provider: ical
     ical_url: "https://calendar.google.com/calendar/ical/..."
   ```
3. Install: `pip install icalendar`

---

## Step 8 — Connect Email (optional)

### Gmail

1. In Google Cloud Console, enable the **Gmail API** (same project as calendar if using Google)
2. Add `gmail.readonly` scope to your OAuth credentials
3. Install: `pip install google-api-python-client` (already done if using Google Calendar)
4. Set `email.enabled: true` and `email.provider: gmail` in `config/config.yaml`

### Microsoft Outlook

1. Add `Mail.Read` permission to your Azure app (same app as calendar if using Microsoft)
2. Set `email.provider: microsoft` in `config/config.yaml`

### Generic IMAP

1. Add to `config/secrets/.env`:
   ```
   IMAP_HOST=imap.yourmail.com
   IMAP_PORT=993
   IMAP_USER=your@email.com
   IMAP_PASS=your-password
   ```
2. Install: `pip install imap-tools`
3. Set `email.provider: imap` in `config/config.yaml`

---

## Step 9 — Connect External Agent Directories (optional)

If you have other agentic AI directories you want the agent to pull context from:

1. In `config/config.yaml`, set `external_agents.enabled: true`
2. Add each source under `external_agents.sources`:

```yaml
external_agents:
  enabled: true
  sources:
    - name: "My Other Agent"
      type: "local"
      path: "/path/to/other/agent/directory"
      read_files: ["tasks.json", "README.md"]
```

---

## Step 10 — Set up scheduling

### macOS (launchd — recommended)

Create a plist file at `~/Library/LaunchAgents/com.agentichelpers.daily.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.agentichelpers.daily</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/agenticHelpers/runner/runner.py</string>
        <string>--task</string>
        <string>daily_briefing</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>7</integer>
        <key>Minute</key>
        <integer>30</integer>
    </dict>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
```

Load it:
```bash
launchctl load ~/Library/LaunchAgents/com.agentichelpers.daily.plist
```

### Linux / macOS (cron)

```bash
crontab -e
```

Add:
```
30 7 * * 1-5 cd /path/to/agenticHelpers && python runner/runner.py --task daily_briefing >> data/logs/cron.log 2>&1
```

### Windows (Task Scheduler)

1. Open Task Scheduler
2. Create Basic Task → name it "agenticHelpers Daily Briefing"
3. Trigger: Daily at 07:30
4. Action: Start a program
   - Program: `python`
   - Arguments: `runner/runner.py --task daily_briefing`
   - Start in: `C:\path\to\agenticHelpers`

### GitHub Actions (runs in the cloud — no local scheduler needed)

Create `.github/workflows/daily_briefing.yml` in your repo (you'll need to add secrets for your API keys in the GitHub repo settings):

```yaml
name: Daily Briefing
on:
  schedule:
    - cron: '30 21 * * 0-4'  # 07:30 AEST = 21:30 UTC previous day
  workflow_dispatch:

jobs:
  briefing:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r runner/requirements.txt
      - run: python runner/runner.py --task daily_briefing
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

---

## Step 11 — Configure output delivery

In `config/config.yaml`, set how the briefing is delivered:

```yaml
briefing:
  delivery:
    method: "email"          # email | file | stdout | webhook
    recipient: "your@email.com"
```

For email delivery, add SMTP settings to `config/secrets/.env`:
```
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your@gmail.com
SMTP_PASS=your-app-password
```

> For Gmail, use an [App Password](https://myaccount.google.com/apppasswords), not your account password.

---

## Setup Complete

Run the agent manually to confirm everything works:

```bash
python runner/runner.py --task daily_briefing
```

Your first briefing will be generated and delivered.

---

## Troubleshooting

**"config/config.yaml not found"** — Copy the example: `cp config/config.example.yaml config/config.yaml`

**"anthropic package not installed"** — Run: `pip install anthropic`

**"Calendar not connected"** — Set `calendar.enabled: true` in config and follow Step 7

**AI gives poor estimates** — The learning store needs data. After ~10 completed tasks, estimates improve significantly.

**Briefing is too long / too short** — Edit `prompts/daily_briefing.md` to adjust the sections and level of detail.
