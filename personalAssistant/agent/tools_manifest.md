# Tools Manifest

This file defines all the external integrations and tools the agent uses. Each integration has a **status**, **purpose**, and **setup reference**.

Update this file whenever you add, change, or remove an integration.

---

## Integration Status Key

| Symbol | Meaning |
|---|---|
| ✅ | Connected and active |
| 🔧 | Configured but not yet tested |
| ❌ | Not connected — setup required |
| ⏸ | Disabled / paused |

---

## Integrations

### 📅 Calendar
| Field | Value |
|---|---|
| Status | ❌ |
| Provider | _e.g. Google Calendar / Microsoft Outlook / Apple Calendar_ |
| Access method | _e.g. Google Calendar API / Microsoft Graph API / CalDAV_ |
| Credentials location | `config/secrets/.env` |
| Setup guide | `SETUP.md` → Calendar section |
| Data used for | Daily briefing, timeline awareness, meeting prep |

---

### 📧 Email
| Field | Value |
|---|---|
| Status | ❌ |
| Provider | _e.g. Gmail / Outlook / IMAP_ |
| Access method | _e.g. Gmail API / Microsoft Graph API / IMAP_ |
| Credentials location | `config/secrets/.env` |
| Setup guide | `SETUP.md` → Email section |
| Data used for | Action items, reply tracking, context |

---

### ✅ To-Do List
| Field | Value |
|---|---|
| Status | ✅ |
| Provider | Local file |
| Access method | JSON file read/write |
| File location | `data/tasks/todo.json` |
| Setup guide | None — works out of the box |
| Data used for | Task tracking, daily focus list |

---

### 📁 Project Files
| Field | Value |
|---|---|
| Status | ✅ |
| Provider | Local files |
| Access method | Markdown/text file read |
| File location | `data/projects/` |
| Setup guide | `SETUP.md` → Project Files section |
| Data used for | Task generation, context, timeline building |

---

### 👤 Coworker Profiles
| Field | Value |
|---|---|
| Status | ✅ |
| Provider | Local files |
| Access method | Markdown/YAML file read |
| File location | `data/profiles/` |
| Setup guide | `SETUP.md` → Coworker Profiles section |
| Data used for | Collaboration recommendations, communication context |

---

### 🤖 External Agent Directories
| Field | Value |
|---|---|
| Status | ❌ |
| Provider | Configurable — local paths or remote URLs |
| Access method | File system or HTTP |
| Configuration | `config/config.yaml` → `external_agents` section |
| Setup guide | `SETUP.md` → External Agents section |
| Data used for | Additional task context, cross-agent coordination |

---

### 🧠 Time Learning Store
| Field | Value |
|---|---|
| Status | ✅ |
| Provider | Local file |
| Access method | JSON file read/write |
| File location | `data/learning/time_estimates.json` |
| Setup guide | None — auto-populated by agent |
| Data used for | Improving future time estimates |

---

## Adding a New Integration

1. Add a new section to this file following the format above.
2. Add required credentials to `config/secrets/.env` (never commit this file).
3. Add the integration connection logic to `runner/runner.py` under the `connect_integrations()` function.
4. Update `SETUP.md` with setup instructions for the new integration.
5. Test by running `python runner/runner.py --dry-run`.
