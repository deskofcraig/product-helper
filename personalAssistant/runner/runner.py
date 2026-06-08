#!/usr/bin/env python3
"""
agenticHelpers — Personal Assistant Agent Runner
AI-tool agnostic orchestration script.

Usage:
    python runner/runner.py --task daily_briefing
    python runner/runner.py --task weekly_review
    python runner/runner.py --task task_breakdown --project "data/projects/my_project.md"
    python runner/runner.py --task update_tasks --updates "task-001 is done, took 90 minutes"
    python runner/runner.py --dry-run
"""

import argparse
import json
import logging
import os
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

# ─────────────────────────────────────────
# Paths
# ─────────────────────────────────────────
ROOT = Path(__file__).parent.parent
CONFIG_FILE = ROOT / "config" / "config.yaml"
USER_PROFILE_FILE = ROOT / "config" / "user_profile.yaml"
TODO_FILE = ROOT / "data" / "tasks" / "todo.json"
LEARNING_FILE = ROOT / "data" / "learning" / "time_estimates.json"
SYSTEM_PROMPT_FILE = ROOT / "agent" / "system_prompt.md"
PROMPTS_DIR = ROOT / "prompts"
PROFILES_DIR = ROOT / "data" / "profiles"
PROJECTS_DIR = ROOT / "data" / "projects"
OUTPUT_DIR = ROOT / "data" / "output"


# ─────────────────────────────────────────
# Logging
# ─────────────────────────────────────────
def setup_logging(config: dict) -> None:
    log_cfg = config.get("logging", {})
    log_file = ROOT / log_cfg.get("file", "data/logs/agent.log")
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=getattr(logging, log_cfg.get("level", "INFO")),
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout),
        ],
    )


# ─────────────────────────────────────────
# Config
# ─────────────────────────────────────────
def load_config() -> dict:
    if not CONFIG_FILE.exists():
        sys.exit(
            f"[ERROR] config/config.yaml not found. "
            f"Copy config/config.example.yaml to config/config.yaml and fill in your values."
        )
    with open(CONFIG_FILE) as f:
        return yaml.safe_load(f)


def load_user_profile() -> dict:
    if not USER_PROFILE_FILE.exists():
        return {}
    with open(USER_PROFILE_FILE) as f:
        return yaml.safe_load(f)


# ─────────────────────────────────────────
# AI Provider — agnostic interface
# ─────────────────────────────────────────
def get_ai_client(config: dict):
    """
    Return an AI client based on config. Supports:
      - anthropic  (Claude)
      - openai     (GPT-4 etc.)
      - google     (Gemini)
      - azure_openai
      - ollama     (local models)

    Add your own provider by implementing the same interface:
        client.complete(system_prompt, user_prompt) -> str
    """
    provider = config["ai"]["provider"].lower()
    model = config["ai"]["model"]
    max_tokens = config["ai"].get("max_tokens", 4096)
    temperature = config["ai"].get("temperature", 0.3)

    env_file = ROOT / "config" / "secrets" / ".env"
    if env_file.exists():
        from dotenv import load_dotenv
        load_dotenv(env_file)

    if provider == "anthropic":
        try:
            import anthropic
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            client = anthropic.Anthropic(api_key=api_key)
            def complete(system_prompt: str, user_prompt: str) -> str:
                response = client.messages.create(
                    model=model,
                    max_tokens=max_tokens,
                    system=system_prompt,
                    messages=[{"role": "user", "content": user_prompt}],
                )
                return response.content[0].text
            return complete
        except ImportError:
            sys.exit("[ERROR] anthropic package not installed. Run: pip install anthropic")

    elif provider == "openai":
        try:
            from openai import OpenAI
            api_key = os.environ.get("OPENAI_API_KEY")
            client = OpenAI(api_key=api_key)
            def complete(system_prompt: str, user_prompt: str) -> str:
                response = client.chat.completions.create(
                    model=model,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                )
                return response.choices[0].message.content
            return complete
        except ImportError:
            sys.exit("[ERROR] openai package not installed. Run: pip install openai")

    elif provider == "google":
        try:
            import google.generativeai as genai
            api_key = os.environ.get("GOOGLE_API_KEY")
            genai.configure(api_key=api_key)
            gemini_model = genai.GenerativeModel(model)
            def complete(system_prompt: str, user_prompt: str) -> str:
                combined = f"{system_prompt}\n\n{user_prompt}"
                response = gemini_model.generate_content(combined)
                return response.text
            return complete
        except ImportError:
            sys.exit("[ERROR] google-generativeai package not installed. Run: pip install google-generativeai")

    elif provider == "azure_openai":
        try:
            from openai import AzureOpenAI
            client = AzureOpenAI(
                api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
                api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01"),
                azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            )
            def complete(system_prompt: str, user_prompt: str) -> str:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                )
                return response.choices[0].message.content
            return complete
        except ImportError:
            sys.exit("[ERROR] openai package not installed. Run: pip install openai")

    elif provider == "ollama":
        try:
            import ollama
            def complete(system_prompt: str, user_prompt: str) -> str:
                response = ollama.chat(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                )
                return response["message"]["content"]
            return complete
        except ImportError:
            sys.exit("[ERROR] ollama package not installed. Run: pip install ollama")

    else:
        sys.exit(f"[ERROR] Unknown AI provider: {provider}. See config/config.example.yaml for supported providers.")


# ─────────────────────────────────────────
# Data loaders
# ─────────────────────────────────────────
def load_todo() -> list:
    if not TODO_FILE.exists():
        return []
    with open(TODO_FILE) as f:
        return json.load(f)


def save_todo(tasks: list) -> None:
    TODO_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def load_learning_store() -> dict:
    if not LEARNING_FILE.exists():
        return {}
    with open(LEARNING_FILE) as f:
        return json.load(f)


def save_learning_store(store: dict) -> None:
    LEARNING_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LEARNING_FILE, "w") as f:
        json.dump(store, f, indent=2)


def load_system_prompt() -> str:
    with open(SYSTEM_PROMPT_FILE) as f:
        return f.read()


def load_prompt(prompt_name: str) -> str:
    prompt_file = PROMPTS_DIR / f"{prompt_name}.md"
    if not prompt_file.exists():
        sys.exit(f"[ERROR] Prompt file not found: {prompt_file}")
    with open(prompt_file) as f:
        return f.read()


def load_profiles() -> list:
    profiles = []
    if PROFILES_DIR.exists():
        for f in PROFILES_DIR.glob("*.yaml"):
            with open(f) as fh:
                profiles.append(yaml.safe_load(fh))
        for f in PROFILES_DIR.glob("*.json"):
            with open(f) as fh:
                profiles.append(json.load(fh))
    return profiles


def load_projects() -> list:
    projects = []
    if PROJECTS_DIR.exists():
        for f in PROJECTS_DIR.glob("*"):
            if f.suffix in [".md", ".txt", ".yaml", ".json"]:
                with open(f) as fh:
                    projects.append({"file": f.name, "content": fh.read()})
    return projects


def load_external_agents(config: dict) -> str:
    """Pull context from external agent directories."""
    ext_cfg = config.get("external_agents", {})
    if not ext_cfg.get("enabled"):
        return ""

    context_parts = []
    for source in ext_cfg.get("sources", []):
        if source["type"] == "local":
            path = Path(source["path"])
            for read_file in source.get("read_files", []):
                target = path / read_file
                if target.exists():
                    with open(target) as f:
                        context_parts.append(
                            f"=== External Agent: {source['name']} / {read_file} ===\n{f.read()}"
                        )
        elif source["type"] == "http":
            try:
                import urllib.request
                headers = {}
                auth_env = source.get("auth_header_env")
                if auth_env:
                    headers["Authorization"] = f"Bearer {os.environ.get(auth_env, '')}"
                for read_file in source.get("read_files", []):
                    url = f"{source['url'].rstrip('/')}/{read_file}"
                    req = urllib.request.Request(url, headers=headers)
                    with urllib.request.urlopen(req) as resp:
                        context_parts.append(
                            f"=== External Agent: {source['name']} / {read_file} ===\n{resp.read().decode()}"
                        )
            except Exception as e:
                logging.warning(f"Could not fetch from external agent {source['name']}: {e}")

    return "\n\n".join(context_parts)


# ─────────────────────────────────────────
# Calendar & Email (stub — connect your provider)
# ─────────────────────────────────────────
def fetch_calendar(config: dict) -> str:
    """
    Fetch calendar events. Connect your calendar provider here.
    Returns a plain-text representation of events.

    See SETUP.md for connection instructions.
    """
    if not config.get("calendar", {}).get("enabled"):
        return "[Calendar not connected — see SETUP.md]"

    provider = config["calendar"]["provider"]

    if provider == "google":
        # Install: pip install google-api-python-client google-auth
        # See SETUP.md → Calendar section
        raise NotImplementedError("Connect Google Calendar — see SETUP.md")

    elif provider == "microsoft":
        # Install: pip install O365
        # See SETUP.md → Calendar section
        raise NotImplementedError("Connect Microsoft Calendar — see SETUP.md")

    elif provider == "ical":
        ical_url = config["calendar"].get("ical_url", "")
        if ical_url:
            try:
                from icalendar import Calendar
                import urllib.request
                with urllib.request.urlopen(ical_url) as resp:
                    cal = Calendar.from_ical(resp.read())
                events = []
                today = date.today()
                for component in cal.walk():
                    if component.name == "VEVENT":
                        dtstart = component.get("dtstart").dt
                        if hasattr(dtstart, "date"):
                            dtstart = dtstart.date()
                        if dtstart >= today:
                            events.append(
                                f"{dtstart} {component.get('dtstart').dt.strftime('%H:%M') if hasattr(component.get('dtstart').dt, 'strftime') else ''} — {component.get('summary')}"
                            )
                return "\n".join(sorted(events[:50]))
            except ImportError:
                return "[icalendar package not installed — run: pip install icalendar]"

    return "[Calendar not connected]"


def fetch_email(config: dict) -> str:
    """
    Fetch actionable emails. Connect your email provider here.
    Returns a plain-text summary of emails.

    See SETUP.md for connection instructions.
    """
    if not config.get("email", {}).get("enabled"):
        return "[Email not connected — see SETUP.md]"

    provider = config["email"]["provider"]

    if provider == "gmail":
        raise NotImplementedError("Connect Gmail — see SETUP.md")

    elif provider == "outlook":
        raise NotImplementedError("Connect Outlook — see SETUP.md")

    elif provider == "imap":
        raise NotImplementedError("Connect IMAP — see SETUP.md")

    return "[Email not connected]"


# ─────────────────────────────────────────
# Task runners
# ─────────────────────────────────────────
def run_daily_briefing(complete, config: dict, user_profile: dict, dry_run: bool = False) -> str:
    logging.info("Running daily briefing...")

    system_prompt = load_system_prompt()
    briefing_prompt = load_prompt("daily_briefing")

    today = date.today()
    user_prompt = briefing_prompt \
        .replace("{{DATE}}", today.strftime("%d %B %Y")) \
        .replace("{{DAY_OF_WEEK}}", today.strftime("%A")) \
        .replace("{{USER_NAME}}", user_profile.get("name", "there")) \
        + f"\n\n## Calendar\n{fetch_calendar(config)}" \
        + f"\n\n## Email\n{fetch_email(config)}" \
        + f"\n\n## Tasks\n{json.dumps(load_todo(), indent=2)}" \
        + f"\n\n## Coworker Profiles\n{json.dumps(load_profiles(), indent=2)}" \
        + f"\n\n## External Agent Context\n{load_external_agents(config)}"

    if dry_run:
        logging.info("[DRY RUN] Would call AI with prompts. Skipping.")
        return "[DRY RUN] Daily briefing would be generated here."

    result = complete(system_prompt, user_prompt)
    deliver_output(result, "daily_briefing", config)
    return result


def run_weekly_review(complete, config: dict, user_profile: dict, dry_run: bool = False) -> str:
    logging.info("Running weekly review...")

    system_prompt = load_system_prompt()
    review_prompt = load_prompt("weekly_review")

    today = date.today()
    user_prompt = review_prompt \
        .replace("{{WEEK_START_DATE}}", today.strftime("%d %b %Y")) \
        .replace("{{WEEK_END_DATE}}", today.strftime("%d %b %Y")) \
        .replace("{{TASK_LIST_JSON}}", json.dumps(load_todo(), indent=2)) \
        .replace("{{TIME_ESTIMATES_JSON}}", json.dumps(load_learning_store(), indent=2)) \
        + f"\n\n## Calendar This Week\n{fetch_calendar(config)}"

    if dry_run:
        logging.info("[DRY RUN] Would call AI with prompts. Skipping.")
        return "[DRY RUN] Weekly review would be generated here."

    result = complete(system_prompt, user_prompt)
    deliver_output(result, "weekly_review", config)
    return result


def run_task_breakdown(complete, config: dict, project_file: str, dry_run: bool = False) -> str:
    logging.info(f"Running task breakdown for: {project_file}")

    system_prompt = load_system_prompt()
    breakdown_prompt = load_prompt("task_breakdown")

    project_content = Path(project_file).read_text() if Path(project_file).exists() else "[Project file not found]"
    today = date.today()

    user_prompt = breakdown_prompt \
        .replace("{{PROJECT_OR_WORK_DESCRIPTION}}", project_content) \
        .replace("{{START_DATE}}", today.strftime("%Y-%m-%d")) \
        .replace("{{TARGET_DATE}}", "[Specify target date]") \
        .replace("{{HOURS_PER_DAY}}", str(config.get("user", {}).get("working_hours", {}).get("hours_per_day", 8))) \
        .replace("{{STAKEHOLDERS}}", "[Specify stakeholders]") \
        .replace("{{KNOWN_DEPENDENCIES}}", "None") \
        .replace("{{PROJECT_ID}}", Path(project_file).stem) \
        .replace("{{TODAY}}", today.strftime("%Y-%m-%d")) \
        + f"\n\n## Historical Estimates\n{json.dumps(load_learning_store(), indent=2)}"

    if dry_run:
        return "[DRY RUN] Task breakdown would be generated here."

    result = complete(system_prompt, user_prompt)
    deliver_output(result, "task_breakdown", config)
    return result


def run_update_tasks(complete, config: dict, updates: str, dry_run: bool = False) -> str:
    logging.info("Running task update...")

    system_prompt = load_system_prompt()
    update_prompt = load_prompt("task_update")
    today = date.today()

    user_prompt = update_prompt \
        .replace("{{CURRENT_TASK_LIST_JSON}}", json.dumps(load_todo(), indent=2)) \
        .replace("{{USER_UPDATES}}", updates) \
        .replace("{{TODAY}}", today.strftime("%Y-%m-%d"))

    if dry_run:
        return "[DRY RUN] Task update would be applied here."

    result = complete(system_prompt, user_prompt)
    # TODO: Parse the JSON from the result and save back to todo.json
    # and update the learning store
    deliver_output(result, "task_update", config)
    return result


# ─────────────────────────────────────────
# Output delivery
# ─────────────────────────────────────────
def deliver_output(content: str, task_name: str, config: dict) -> None:
    briefing_cfg = config.get("briefing", {})
    method = briefing_cfg.get("delivery", {}).get("method", "file")

    # Always save to file
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"{task_name}_{timestamp}.md"
    output_file.write_text(content)
    logging.info(f"Output saved to: {output_file}")

    if method == "email":
        recipient = briefing_cfg.get("delivery", {}).get("recipient")
        if recipient:
            send_email(content, task_name, recipient, config)

    elif method == "stdout":
        print(content)

    elif method == "webhook":
        webhook_url = briefing_cfg.get("delivery", {}).get("webhook_url")
        if webhook_url:
            send_webhook(content, webhook_url)


def send_email(content: str, subject_prefix: str, recipient: str, config: dict) -> None:
    """Send output via email. Configure SMTP in config/secrets/.env."""
    import smtplib
    from email.mime.text import MIMEText

    smtp_host = os.environ.get("SMTP_HOST", "")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    smtp_user = os.environ.get("SMTP_USER", "")
    smtp_pass = os.environ.get("SMTP_PASS", "")

    if not smtp_host:
        logging.warning("SMTP not configured — output saved to file only. See SETUP.md.")
        return

    msg = MIMEText(content, "plain")
    msg["Subject"] = f"[Assistant] {subject_prefix.replace('_', ' ').title()} — {date.today()}"
    msg["From"] = smtp_user
    msg["To"] = recipient

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        logging.info(f"Email sent to {recipient}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")


def send_webhook(content: str, url: str) -> None:
    """Send output to a webhook (e.g. Slack, Teams, n8n)."""
    import json
    import urllib.request
    payload = json.dumps({"text": content}).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req)
        logging.info(f"Webhook delivered to {url}")
    except Exception as e:
        logging.error(f"Webhook delivery failed: {e}")


# ─────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="agenticHelpers — Personal Assistant Agent")
    parser.add_argument("--task", choices=["daily_briefing", "weekly_review", "task_breakdown", "update_tasks"], help="Task to run")
    parser.add_argument("--project", help="Path to project file (for task_breakdown)")
    parser.add_argument("--updates", help="Task update string (for update_tasks)")
    parser.add_argument("--dry-run", action="store_true", help="Run without calling the AI or saving changes")
    args = parser.parse_args()

    config = load_config()
    setup_logging(config)
    user_profile = load_user_profile()

    logging.info(f"agenticHelpers starting — task: {args.task or 'none'}")

    if args.dry_run:
        logging.info("DRY RUN mode enabled")
        # Test integrations and config without calling AI
        logging.info(f"Config loaded: provider={config['ai']['provider']}, model={config['ai']['model']}")
        logging.info(f"Todo tasks: {len(load_todo())}")
        logging.info(f"Profiles: {len(load_profiles())}")
        logging.info(f"Projects: {len(load_projects())}")
        logging.info("Dry run complete — all config and data files read successfully.")
        return

    complete = get_ai_client(config)

    if args.task == "daily_briefing":
        result = run_daily_briefing(complete, config, user_profile)
        print(result)

    elif args.task == "weekly_review":
        result = run_weekly_review(complete, config, user_profile)
        print(result)

    elif args.task == "task_breakdown":
        if not args.project:
            sys.exit("[ERROR] --project is required for task_breakdown")
        result = run_task_breakdown(complete, config, args.project)
        print(result)

    elif args.task == "update_tasks":
        updates = args.updates or input("Describe task updates: ")
        result = run_update_tasks(complete, config, updates)
        print(result)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
