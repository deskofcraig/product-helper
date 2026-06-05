# product-skills — Setup and Usage Guide

## Installation

Each skill is a separate installable `.skill` file. Install via **Settings → Capabilities → Skills → Install skill**.

| Skill | File | Install if you are... |
|---|---|---|
| `product-strategy` | `product-strategy/product-strategy.skill` | Working on strategic direction, opportunity framing, or 'why now' decisions |
| `product-manager` | `product-manager/product-manager.skill` | Running discovery, defining requirements, or managing scope |
| `product-designer` | `product-designer/product-designer.skill` | Working on any design phase from kick-off through engineering handoff |

Install all three if you work cross-functionally or review work across multiple disciplines.

---

## Basic usage

Invoke a skill by typing its name in a chat, then share your document or describe your situation.

```
product-strategy

[paste or describe your work]
```

The skill reads what you've shared, detects the appropriate mode (kick-off, check-in, handover, or analysis), and runs the relevant checkpoint.

---

## The four modes in detail

### Kick-off

**Trigger phrases:** "We're starting", "kick off", "about to begin", "just received this"

**What happens:** The skill runs structured questions before work begins — orienting the problem, confirming prerequisites, surfacing assumptions, and identifying what needs to be answered before the team can proceed with confidence.

Questions are asked in rounds (not all at once). Answer each round before the next is presented.

**Example:**
```
product-manager

Kick-off. We've just received a strategy brief asking us to improve the onboarding experience for new Octopus users. Starting discovery this week.
```

---

### Check-in

**Trigger phrases:** "Is this on track?", "quick review", "am I missing anything?", "check in"

**What happens:** The skill evaluates work in progress against quality benchmarks. It identifies gaps before they compound — missing evidence, weak assumptions, incomplete requirements — and tells you specifically what to address.

**Example:**
```
product-designer

Check in. [paste current wireframes description or design brief]
```

---

### Handover

**Trigger phrases:** "Handing this to", "ready to hand over?", "is this ready for", "passing to the next stage"

**What happens:** The skill runs a full MQB (Minimum Quality Bar) gate. It checks all required deliverables against the handover checklist and gives a pass/fail with specific items blocking progress.

**Example:**
```
product-manager

Handing to design. Here's our brief: [paste brief]
```

The skill will tell you exactly what's present, what's missing, and what must be resolved before the handover is valid.

---

### Analysis

**Trigger:** Sharing a complete or near-complete document without a specific mode instruction

**What happens:** Full structured assessment of the document against best practice benchmarks — signal quality audit, insight chain trace, assumption map, gap register, and candidate directions.

**Example:**
```
product-strategy

[paste a complete strategy document or brief]
```

---

## Handover MQB reference

These are the non-negotiable items at each stage transition. If any are missing, the handover is blocked.

### Strategy → PM

| Item | Required |
|---|---|
| Goal | Outcome stated — what changes, not what gets built |
| Problem statement | User + barrier + impact, solution-free |
| Why now | Specific urgency signal or strategic window |
| Scope boundaries | What is and isn't in scope |

---

### PM → Design

| Item | Required |
|---|---|
| Problem statement | Validated with evidence, solution-free |
| User needs | Ranked by priority, with supporting signal |
| Success metrics | Measurable, tied to the problem |
| V1 scope | Explicitly defined, with out-of-scope documented |
| Known constraints | Technical, business, accessibility |

---

### Design → Engineering

| Item | Required |
|---|---|
| All screen states | Default, loading, empty, error, success |
| User flows | Happy path, error path, empty state path |
| Annotations | Behaviour descriptions on every non-obvious interaction |
| Component spec | What components are used, what needs to be built |
| Accessibility basics | Colour contrast, focus order, ARIA labels where needed |

---

## Using TASKS.md files

Each skill folder contains a `TASKS.md` — a stage-by-stage checklist of everything to complete before progressing. These are designed to be used alongside the skill.

To use one: open it in any markdown viewer, or paste its contents into a chat and ask the relevant skill to review your progress against it.

---

## Worked example — full flow

**Week 1: Strategy kick-off**
```
product-strategy
Kick-off. We've been asked to explore an opportunity around deployment visibility for enterprise customers.
```
→ Strategy skill asks 15 structured questions across context, goal, constraints, and assumptions.

**Week 3: PM handover check**
```
product-strategy
Handing to PM. Here's what we have: [paste strategy doc]
```
→ Strategy skill runs MQB gate. Any missing items are flagged before PM work begins.

**Week 4: PM kick-off**
```
product-manager
Kick-off. Received brief from strategy. [paste brief]
```
→ PM skill aligns on the problem statement, plans discovery, surfaces the biggest unknowns.

**Week 7: Mid-PM check-in**
```
product-manager
Check in. Here's where we are after discovery: [paste research synthesis]
```
→ PM skill assesses discovery quality, requirement completeness, design readiness.

**Week 8: Design handover**
```
product-manager
Handing to design. [paste full PM brief]
```
→ PM skill runs the PM→Design MQB gate. Pass/fail with specific gaps called out.
