# product-advisor — Setup and Usage Guide

## Installation

Install via **Settings → Capabilities → Skills → Install skill**, selecting `product-advisor/product-advisor.skill`.

`product-advisor` depends on both sub-suites. For it to work correctly, also install all skills from `product-skills/` and `role-lenses/`, and keep the `product-helper/` folder structure intact.

**Full install list:**

| Skill | Location |
|---|---|
| `product-advisor` | `product-advisor/product-advisor.skill` |
| `product-strategy` | `product-skills/product-strategy/product-strategy.skill` |
| `product-manager` | `product-skills/product-manager/product-manager.skill` |
| `product-designer` | `product-skills/product-designer/product-designer.skill` |
| `design-lens` | `role-lenses/design-lens/design-lens.skill` |
| `pm-lens` | `role-lenses/pm-lens/pm-lens.skill` |
| `eng-lens` | `role-lenses/eng-lens/eng-lens.skill` |

---

## Basic usage

Type `product-advisor` in a chat and share your document. That's it — the skill determines what to run.

```
product-advisor

[paste your document, brief, pitch, goal, or work description]
```

If your intent is clear from the document (e.g. it's a near-complete strategy doc), the skill selects the most useful analysis automatically. If it's ambiguous, it will ask one clarifying question before proceeding.

---

## Directing the analysis

You can steer the skill toward a specific route by including a short instruction alongside your document.

### Full combined review (process quality + seniority perspective)

```
product-advisor

Full review. [paste document]
```

Runs the relevant `product-skills` mode and the matching `role-lenses` level detection in sequence, then produces a synthesis showing where the two analyses agree and what each adds.

---

### Process quality only

```
product-advisor

Process quality check. [paste document]
```

Routes to the relevant `product-skills` skill (strategy, PM, or designer) and the appropriate mode (kick-off, check-in, handover, or analysis).

---

### Seniority perspective only

```
product-advisor

Level check. [paste document]
```

Routes to the relevant `role-lenses` skill, detects the level, and applies that persona's task breakdown, questions, and risks.

---

### Handover readiness

```
product-advisor

Is this ready to hand to [design / engineering / PM]? [paste document]
```

Routes to the relevant `product-skills` handover mode and runs the MQB gate. Returns a pass/fail with specific items blocking the handover.

---

### Routing guidance only

```
product-advisor

Which skill should I use for this? [describe or paste your work]
```

Returns a routing recommendation — the specific sub-skill and mode most useful for your situation — without running a full analysis.

---

### Cross-functional review

```
product-advisor

Cross-functional review. [paste document]
```

Runs all three role-lenses (Design, PM, Engineering) against the document, then produces a consolidated view: what each discipline prioritises, where they agree, where they diverge, and what the handover chain looks like.

---

## Understanding the output

### For a full combined review (Route C)

```
STAGE IN THE CHAIN
[Where the work sits: Strategy / PM / Design / cross-phase]

SENIORITY READ
[Initial level signal before formal detection]

--- PROCESS QUALITY LAYER ---
[Mode, checkpoint output, MQB status, gaps from product-skills]

--- SENIORITY PERSPECTIVE LAYER ---
[Level detected, questions, task breakdown, risks, definition of done, push-back]

--- SYNTHESIS ---
Where the two analyses align: [highest-confidence findings]
Where they add to each other: [what each layer contributes]
Recommended next skill: [specific sub-skill + mode + one-line rationale]
```

### For a cross-functional review (Route E)

```
STAGE IN THE CHAIN

PROCESS QUALITY CHECK
[product-skills output for the relevant stage]

DESIGN LENS
[design-lens output]

PM LENS
[pm-lens output]

ENGINEERING LENS
[eng-lens output]

CROSS-FUNCTIONAL SYNTHESIS
Where all three agree: [highest-confidence gaps or risks]
Where disciplines diverge: [tensions to resolve]
Handover readiness: [what can move forward and what is blocked]
```

Every response ends with a **recommended next skill** — never a dead end.

---

## Worked examples

### Example 1 — You've just received a brief and don't know where to start

```
product-advisor

Just received this. Not sure which skill to use or what to do first.

Goal: Reduce setup time for enterprise customers deploying to multiple cloud targets simultaneously.
Background: This came out of three customer calls last quarter. No formal discovery done yet.
Constraints: Must ship something within one cycle. Engineering capacity is limited.
```

`product-advisor` will identify this as early PM / pre-discovery work, route to `product-strategy` or `product-manager` kick-off mode, and tell you exactly what questions to answer before work begins.

---

### Example 2 — You want to know if your design brief is ready to hand to engineering

```
product-advisor

Is this ready for engineering? [paste design brief]
```

Routes to `product-designer` handover mode, runs the MQB gate (all screen states, flows, annotations, component spec, accessibility), and returns a clear pass or fail with the specific items blocking handover.

---

### Example 3 — You want a full review of a pitch before presenting to leadership

```
product-advisor

Full review. Presenting this to the GLT on Thursday.

[paste pitch]
```

Runs a process quality check (is the strategic case complete?) and a seniority perspective (is this pitched at the right scope for the audience?), then synthesises — telling you what's missing and what the GLT will push back on.

---

### Example 4 — You want a cross-functional read before a team kick-off

```
product-advisor

Cross-functional review before we kick off next week.

[paste brief or goals document]
```

Runs Design, PM, and Engineering lenses against the document. The consolidated output shows what each function will ask at kick-off, where their concerns align, and what tensions need to be resolved before work starts.

---

## Tips

**You don't need to know which sub-skill to use.** That's the point of `product-advisor`. Share what you have and let it route.

**The synthesis is the most valuable part of a full review.** The individual analyses from `product-skills` and `role-lenses` are available in those sub-skills directly. What `product-advisor` adds is the cross-layer synthesis — where a process gap is explained by a seniority framing issue, or where an ambitious level read is blocked by missing MQB items.

**Use the recommended next skill.** Every `product-advisor` response ends with a specific sub-skill recommendation. Following it takes you from orientation to depth in one step.

**Run it again after you've addressed gaps.** `product-advisor` is useful at multiple points — after addressing feedback, before a new handover, or when the work has shifted in scope.
