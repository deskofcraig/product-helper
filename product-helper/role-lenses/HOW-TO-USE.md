# role-lenses — Setup and Usage Guide

## Installation

Each lens is a separate installable `.skill` file. Install via **Settings → Capabilities → Skills → Install skill**.

| Skill | File | Install if you are... |
|---|---|---|
| `design-lens` | `design-lens/design-lens.skill` | A designer, design manager, or director at any level |
| `pm-lens` | `pm-lens/pm-lens.skill` | A PM, Senior PM, Principal PM, or Director |
| `eng-lens` | `eng-lens/eng-lens.skill` | An engineer at any level |

Install all three if you review cross-functional work or want to run multi-discipline analysis.

---

## Basic usage

Invoke a lens by typing its name in a chat, then paste or describe your document.

```
design-lens

[paste your brief, goal, pitch, or work description]
```

The lens reads the document, detects the appropriate level, and returns a five-part analysis calibrated to that level.

---

## What the lens detects

Before applying a persona, each lens scores your document across five signal dimensions:

| Dimension | What it reads |
|---|---|
| **Scope** | Is this a single feature, a cross-team initiative, a portfolio-level bet, or company strategy? |
| **Impact horizon** | Are we talking about this cycle, this half, next year, or multi-year? |
| **Stakeholders** | Is this team-internal, group-level, executive, or board/market-facing? |
| **Complexity** | Are requirements well-defined or highly ambiguous? |
| **Work type** | Is this a component, a feature, a program, a platform, or an operating model? |

The level with the best signal match is selected. Mixed signals return a lower confidence rating — which is itself useful information.

---

## Overriding the detected level

If you want a specific level applied regardless of what the skill detects, tell it explicitly:

```
design-lens

Apply the VP lens to this document, regardless of what level you detect.

[paste document]
```

This is useful for:
- Seeing how a more senior stakeholder would read your work before a presentation
- Understanding what an L4 view of an L3-scoped brief reveals
- Exploring what higher scope or ambition would look like for the same problem

---

## Running multiple lenses on the same document

For cross-functional documents (pitches, strategy briefs, goals, OKRs), run all three lenses in sequence. Each discipline will independently detect a level and apply its perspective.

```
design-lens
[paste document]
```

Then:
```
pm-lens
[paste same document]
```

Then:
```
eng-lens
[paste same document]
```

**What this gives you:** A triangulated read across Design, PM, and Engineering — what each discipline prioritises, what they'd push back on, and where they agree or diverge. Different levels are commonly detected across disciplines on the same document, which is informative: a pitch that reads as L4 (Lead) work for Design may read as L5 (Principal) work for Engineering if the architectural implications are large.

---

## Document types that work well

| Document type | What the lens helps with |
|---|---|
| **Feature brief** | Task breakdown at the right scope, risks, definition of done |
| **Pitch / proposal** | Questions the audience will ask, what to pre-empt, what's undersized |
| **Research / discovery doc** | What insight is still missing, how to validate, what the level would prioritise |
| **Goal / OKR** | Whether the goal is level-appropriate, how to measure it, what delivery looks like |
| **Strategy doc** | Cross-portfolio implications, long-term risks, what a VP or Director would want addressed |

---

## Worked examples

### Example 1 — Checking level-appropriateness of a brief

```
pm-lens

Here's the brief I've written for our next cycle:

Goal: Reduce time-to-first-deployment for new users from 4 days to 1 day.
Problem: New users are struggling to configure their first deployment pipeline. Churn is highest in the first 14 days.
Scope: Redesign the onboarding flow for Kubernetes step templates. Out of scope: existing users, non-Kubernetes targets.
Constraints: Cannot change the underlying infrastructure. Must ship within 8 weeks.
```

The lens will detect this as likely **Senior PM** scope (cross-squad initiative, 6-month horizon, customer metric focus) and apply that persona's questions, task breakdown, and push-back.

---

### Example 2 — Understanding what a more senior view adds

```
design-lens

Apply the L5 Principal lens to this document.

[paste a brief that's currently written at L3/L4 scope]
```

The lens will show you what a Principal Designer would see that isn't currently addressed — likely: cross-portfolio implications, missing experience metrics, absence of a north star concept, and patterns that should become reusable.

---

### Example 3 — Pre-flight for a stakeholder presentation

```
eng-lens

I'm presenting this technical direction to the group tomorrow. What would an L5 Principal ask?

[paste your technical direction document]
```

The lens applies the L5 Principal persona and surfaces the questions and push-backs most likely to come up.

---

## Understanding the output

Every lens returns the same five-part structure:

**Level Detected / Confidence / Key signals**
The detected level, how confident the skill is, and the 2–3 signals that drove the conclusion. Low confidence means mixed signals in the document — worth noting.

**Questions this level would ask**
Not generic questions — these are drawn from the detected level's persona and made specific to your document's content.

**How to break down the work**
A concrete, ordered task and activity breakdown at this level's scope. An L3 breakdown focuses on a specific flow; an L5 breakdown focuses on cross-portfolio architecture and reusable patterns.

**Dependencies and risks**
What could go wrong or needs input from others, given the specific document. More senior levels surface broader systemic risks; more junior levels surface immediate execution risks.

**What "done" looks like at this level**
A level-appropriate success definition specific to this work — not generic.

**One thing this level would push back on**
The single most important challenge or reframe. This is often the most useful output — the assumption that, if left unaddressed, will surface as a problem later.

---

## Level quick reference

### design-lens levels

| Level | Detecting signals |
|---|---|
| L3 Senior Designer | Single flow, team scope, cycle horizon, defined requirements |
| L4 Lead Designer | Multi-flow, cross-squad, 6-month horizon, experience architecture questions |
| L5 Principal Designer | Org-wide, 12+ month horizon, "category-defining", cross-portfolio |
| L5 Assoc Director | Portfolio accountability, coaching others, 1–2 year horizon |
| L6 Director | Cross-portfolio, executive stakeholders, 2–3 year vision |
| VP | Company-wide, board/market, 3–5 year, org capacity and design as differentiator |

### pm-lens levels

| Level | Detecting signals |
|---|---|
| Product Manager | Single area, cycle-level, team-internal, defined problem |
| Senior PM | Cross-team, 6–12 month, group managers referenced, hypothesis-testing framing |
| Principal PM | Highly ambiguous, net-new capability, senior leader alignment needed |
| Director | Portfolio, multi-year storyboard, executive/market, PM enablement |

### eng-lens levels

| Level | Detecting signals |
|---|---|
| L2 Software Engineer | Single task, supervised, clear output, current cycle |
| L3 Senior Engineer | Feature-level, team peers, current + next cycle, some ambiguity |
| L4 Lead Engineer | Inception to production, team (5–15), 6–12 months, architectural decisions |
| L5 Principal Engineer | Group-wide, cross-team, 12+ months, technical strategy and target architecture |
