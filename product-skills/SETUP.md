# Setup Instructions

How to install the Product Skills Suite and get the most from each skill.

---

## Requirements

- Access to Claude (claude.ai Pro or Team, or Claude API)
- The skill files from this package (all `.md` format)
- No other tools, integrations, or accounts required

---

## Installation on claude.ai

1. Open [claude.ai](https://claude.ai) → **Settings** → **Skills**
2. Click **Add Skill** or **Import Skill**
3. Upload each `SKILL.md` file individually — you will also be prompted to upload reference files
4. For each skill, upload its three reference files from the `references/` folder:
   - `industry-standards.md`
   - `quality-standards.md`
   - `checkpoint-questions.md`
5. Confirm each installation — all three skills should appear as active

Once installed, Claude selects the appropriate skill automatically based on what you share or ask.

---

## Installation via Claude API

Include the skill and reference content in your system prompt.

```python
import anthropic

def load_skill(skill_name):
    base = f"./{skill_name}"
    parts = []
    with open(f"{base}/SKILL.md") as f:
        parts.append(f.read())
    for ref in ["industry-standards", "quality-standards", "checkpoint-questions"]:
        with open(f"{base}/references/{ref}.md") as f:
            parts.append(f"---\n# Reference: {ref}\n\n" + f.read())
    return "\n\n".join(parts)

client = anthropic.Anthropic()

# Single skill
system = load_skill("product-strategy")

# Or all three
system = "\n\n---\n\n".join([
    load_skill("product-strategy"),
    load_skill("product-manager"),
    load_skill("product-designer"),
])

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    system=system,
    messages=[{"role": "user", "content": "We're kicking off a new product strategy piece..."}]
)
```

---

## Installation on Other AI Platforms

These skills are plain markdown — they work with any LLM that supports system prompts.

1. Copy the contents of the relevant `SKILL.md`
2. Append the contents of the three reference files below it
3. Paste the combined text into the system prompt or instruction field
4. Share or describe your work in the user turn

Compatible with: ChatGPT (custom GPT), Gemini 1.5+, Mistral Large, and capable open-source models (70B+ recommended for structured output quality).

---

## How to Trigger the Right Mode

Each skill runs in four modes. Claude selects the mode based on what you say. You can also
trigger modes explicitly.

### Automatic triggers

| What you say | Mode activated |
|---|---|
| "We're kicking off…", "Starting on…", "Just received a brief…" | Kick-off |
| "Is this on track?", "Quick check…", "What am I missing?" | Check-in |
| "Ready to hand over?", "Is this ready for…?", "Handing to…" | Handover |
| Shares a document or artefact for review | Analysis |

### Explicit triggers

```
"Run a kick-off for this strategy work: [paste brief or description]"

"Check in on my discovery — here's where I am: [paste notes]"

"Is this ready to hand to design? [paste requirements doc]"

"Full analysis of this design brief: [paste or describe]"

"Run all three skills on this: [paste work]"
```

### Specifying the skill explicitly

```
"Product Strategy kick-off: we're about to start exploring [opportunity]"

"Product Manager check-in: here's my discovery so far [paste notes]"

"Product Designer handover to engineering: is this ready? [describe or upload]"
```

---

## What to Share

| You have | How to share it |
|---|---|
| A written brief or document | Paste the text, or upload the file |
| A design screenshot or image | Attach the image directly |
| A rough idea | Describe it — as much or as little as you have |
| Research notes | Paste a summary or the full notes |
| A Whimsical, Figma, Miro, or Notion link | Describe the contents, or screenshot + upload |
| A Slack thread | Copy and paste the relevant messages |
| A verbal "where are we" | Just describe — the skill asks one clarifying question if needed |

More context = more specific output. A one-paragraph description gives a general check-in;
a full document gives a detailed, specific audit.

---

## Customising for Your Team

To add team-specific context without changing the core frameworks, add a short block at the
top of each `SKILL.md`:

```markdown
## Team Context

- Our design system is called [Name]
- We use [Methodology — e.g., dual-track agile, Shape Up]
- Our current strategic goal is [X]
- Our primary user segments are [A, B, C]
- Our standard for "definition of done" in discovery is [X]
- Accessibility standard: WCAG [AA / AAA]
```

This personalises the output while preserving the underlying frameworks.

---

## Using the Quality Gates

Each skill applies a **Minimum Quality Bar (MQB)** at handover. These are not suggestions —
they are gates. If MQB is not met, the skill will tell you the handover is not ready and name
the specific blockers.

| Handover | MQB (must all be present) |
|---|---|
| PS → PM | Goal + Problem statement + Why now + Scope boundaries |
| PM → PD | Problem statement + User needs + Success metrics + V1 scope + Known constraints |
| PD → Eng | All screen states + flows (happy/error/empty) + annotations + component spec + a11y |

You can override the gate if your team has a deliberate reason to proceed. Tell the skill:
*"We are proceeding despite [gap] because [reason]."* It will acknowledge and flag the risk.

---

## Troubleshooting

**The skill isn't activating**
→ Try explicit triggering: "Use the product strategy skill to run a kick-off on this"

**The output is too generic**
→ Share more context — paste the actual document rather than describing it

**Questions feel unnecessary for my context**
→ Tell the skill: "Skip questions — I just want the analysis" or "Assume [X] is already established"

**The MQB gate is blocking something we've deliberately chosen to defer**
→ Say: "We're proceeding without [X] because [reason]" — the skill will document it as a known risk

**I only want part of the output**
→ Ask for specific sections: "Just the assumption map", "Only the gap register", "Just the handover verdict"

**I disagree with a finding**
→ Push back: "I disagree with [point] because [reason]" — the skill will engage with the reasoning

**The drafted elements (goals, problem statements) are off**
→ Expected — they are starting points, not finished versions. Refine them with your team.
