# Daily Briefing Prompt

This prompt is used to generate the daily briefing. Provide it to your AI tool along with the system prompt and the current context data.

---

## Prompt

You are acting as the personal assistant agent defined in `agent/system_prompt.md`.

Today is {{DATE}} ({{DAY_OF_WEEK}}).

Using the following context, generate a daily briefing for the user. The briefing should be structured, scannable, and actionable. It should cover both work and personal areas.

**Context to read:**
- Calendar events for today and the next 3 days
- Unread/unactioned emails (flagged or recent)
- Current to-do list from `data/tasks/todo.json`
- Any overdue tasks
- Project files relevant to today's work
- Coworker profiles for anyone appearing in today's calendar or tasks

---

## Output Structure

Generate the briefing in this exact structure:

---

### 🌅 Good morning, {{USER_NAME}}. Here's your day.

**{{DATE}} — {{DAY_OF_WEEK}}**

---

#### 📅 Today's Calendar
List all calendar events for today with time, title, and any prep notes needed.
Flag any conflicts or back-to-back meetings.

Format:
- `HH:MM` — [Event Title] _(with [Person] if applicable)_
  - **Prep:** [Any prep needed, or "None"]

---

#### 📧 Email Actions Needed
Surface emails that need a reply or action. Group by urgency.

**Reply today:**
- From: [Name] | Subject: [Subject] | [One-line summary of what's needed]

**Review when you can:**
- From: [Name] | Subject: [Subject] | [One-line summary]

---

#### ✅ Today's Task Focus
List the top 5–8 tasks to focus on today, ordered by priority. Include estimated time for each.

Format:
- [ ] [Task name] — ⏱ [Estimated time] | 📁 [Project] | Priority: [High/Medium/Low]

Flag any tasks that are blocked and state what they're blocked by.

---

#### ⚠️ Overdue / At Risk
List any tasks that are overdue or at risk of missing their deadline.

Format:
- ❌ OVERDUE: [Task] — was due [date] | [Project]
- 🟡 AT RISK: [Task] — due [date] | [Why it's at risk]

---

#### 👥 Who to Work With Today
Based on today's tasks and calendar, list the people the user should connect with and why.

Format:
- **[Name]** ([Role]) — [Why / what to discuss or collaborate on]

---

#### 📆 Week Ahead Snapshot
Brief summary of the next 3 days — key deadlines, meetings, and focus areas.

Format:
- **Tomorrow ([Day]):** [Key items]
- **[Day+2]:** [Key items]
- **[Day+3]:** [Key items]

---

#### 🧠 Focus Recommendation
One paragraph summarising where the user's primary focus should be today and why, based on deadlines, meeting load, and task state.

---

#### 📝 Notes
Any other flags, reminders, or context the agent thinks the user should be aware of.

---

## Scheduling Note

This prompt is designed to be run each morning. See `config/schedule.yaml` for scheduling configuration.
