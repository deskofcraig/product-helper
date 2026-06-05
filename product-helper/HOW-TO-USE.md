# Product Helper — Setup and Usage Guide

## Installation

### Step 1 — Install the skills in Claude (Cowork)

Each `.skill` file inside this folder is an installable Claude skill. Install them via:

**Settings → Capabilities → Skills → Install skill**

Install all six skills for the full suite, or install only the ones relevant to your role:

| Skill file | Location | Who needs it |
|---|---|---|
| `product-advisor.skill` | `product-advisor/` | Everyone — this is the entry point |
| `product-strategy.skill` | `product-skills/product-strategy/` | Strategy leads, PMs, Directors |
| `product-manager.skill` | `product-skills/product-manager/` | PMs, Senior PMs, Principal PMs |
| `product-designer.skill` | `product-skills/product-designer/` | Designers at any level |
| `design-lens.skill` | `role-lenses/design-lens/` | Designers, Design Managers, Directors |
| `pm-lens.skill` | `role-lenses/pm-lens/` | PMs, Senior PMs, Principal PMs, Directors |
| `eng-lens.skill` | `role-lenses/eng-lens/` | Engineers at any level |

### Step 2 — Folder structure (required for product-advisor)

For `product-advisor` to reference both suites correctly, keep the folder structure intact:

```
product-helper/
├── product-advisor/
├── product-skills/
└── role-lenses/
```

Do not move individual skill folders outside this structure.

### Step 3 — Verify

In a new chat, type `product-advisor`. Claude should recognise the skill and confirm it's ready.

---

## Choosing where to start

### Use `product-advisor` when:
- You want a full review of a document (process quality + seniority perspective in one response)
- You're not sure which skill is most relevant
- You need a cross-functional view across Design, PM, and Engineering
- You want to know where in the Strategy → PM → Design → Engineering chain your work sits

### Use `product-skills` directly when:
- You want structured kick-off questions before starting a phase of work
- You want a check-in against quality benchmarks mid-work
- You want to verify a handover is ready and MQBs are met
- You want a deep analysis of a document against best practice standards

### Use `role-lenses` directly when:
- You want to understand what a more senior or more junior lens would see in your work
- You want to check whether you're thinking at the right scope and ambition level
- You want to run the same document through all three disciplines for a triangulated view
- You're preparing for a stakeholder conversation and want to anticipate what they'll ask

---

## Common workflows

### Starting a new piece of work

```
product-strategy

[describe the opportunity or problem you've been handed]
```

The `product-strategy` skill will run a kick-off, ask the right questions to orient the work, and tell you what you need to have answered before proceeding.

---

### Checking in on work in progress

```
product-manager

[paste or describe your current brief, discovery findings, or requirements]
```

The skill detects mid-work context and runs a check-in against PM quality benchmarks.

---

### Checking if something is ready to hand over

```
product-designer

Handing this to engineering. [paste your design brief or describe current state]
```

The skill runs a handover check, applies the MQB gate, and tells you exactly what's missing.

---

### Understanding if you're thinking at the right level

```
pm-lens

[paste your brief or goal]
```

The skill detects your level from the document and applies that persona's questions and task breakdown.

---

### Full review — process quality + seniority perspective

```
product-advisor

[paste your document]
```

`product-advisor` runs both suites in combination: a process quality check (is this correct for its stage?) and a seniority perspective (is this the right scope of thinking?), then synthesises the findings.

---

### Cross-functional review (all three disciplines)

```
product-advisor

Full cross-functional review. [paste your document]
```

All three role-lenses run in sequence (Design, PM, Engineering), then a consolidated view shows where disciplines agree, where they diverge, and what the handover chain looks like.

---

## The handover chain

The `product-skills` suite enforces quality gates at each transition. Nothing should move forward until the gate is met.

```
STRATEGY
  ↓
  Gate: Goal + Problem statement + Why now + Scope boundaries
  ↓
PRODUCT MANAGEMENT
  ↓
  Gate: Problem statement + User needs + Success metrics + V1 scope + Known constraints
  ↓
PRODUCT DESIGN
  ↓
  Gate: All screen states + User flows (happy + error + empty) + Annotations +
        Component spec + Accessibility basics
  ↓
ENGINEERING
```

If you're blocked at a gate, use the relevant `product-skills` skill in **handover** mode to identify exactly what's missing.

---

## Quick reference: skill invocation

| What you want | Type this |
|---|---|
| Full review, unsure where to start | `product-advisor` |
| Strategy kick-off or check | `product-strategy` |
| PM discovery kick-off or check | `product-manager` |
| Design kick-off or handover check | `product-designer` |
| Design level + task breakdown | `design-lens` |
| PM level + task breakdown | `pm-lens` |
| Engineering level + task breakdown | `eng-lens` |

---

## Tips

**Paste the document, don't describe it.** All skills are optimised to read real content — briefs, goals, pitches, research docs, strategy documents. The more you share, the more specific the output.

**Run `product-advisor` first if you're unsure.** It reads the document, tells you where it sits in the chain, and recommends which sub-skill to go deeper with.

**Use handover mode as a pre-flight check.** Before presenting to stakeholders or passing work to the next function, run the relevant `product-skills` skill in handover mode. It will catch gaps before they become review comments.

**Low confidence on a role-lens is signal.** If `design-lens` or `pm-lens` returns `Confidence: Low` on level detection, the document has mixed scope signals — worth naming that ambiguity before the work starts.
