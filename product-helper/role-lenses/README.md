# role-lenses

Three Claude skills that analyse any work document through a role-appropriate seniority lens — auto-detecting the right career level from the document and applying that level's mindset, task breakdown, and risk framing.

---

## What this suite does

The role-lenses answer a different question to the `product-skills` suite. Where `product-skills` asks *"is this work done correctly for its stage?"*, role-lenses ask *"is this being thought about at the right level of scope and ambition?"*

Each lens reads signals in your document — scope, impact horizon, stakeholders, complexity, and work type — and matches them to the most appropriate career level. It then applies that level's perspective: the questions they'd naturally ask, how they'd break down the work, what risks they'd see, and what they'd push back on.

This is useful for:
- Checking whether your framing is level-appropriate before a stakeholder conversation
- Understanding what a more senior or more junior view of the same work would reveal
- Calibrating task breakdowns and activity planning to the right scope
- Running a cross-functional document through all three disciplines simultaneously

---

## The three lenses

### `design-lens`

Covers the full Octopus Product Design career ladder.

| Level | Scope | Horizon | Primary focus |
|---|---|---|---|
| L3 Senior Designer | Team | 3–6 months | Own the flow. Quality, system coverage, accessibility |
| L4 Lead Designer | Multi-team | 6–12 months | Experience architecture, cross-squad coherence, metrics |
| L5 Principal Designer | Org-wide | 1–2 years | Category-defining vision, cross-portfolio patterns |
| L5 Assoc Director | Portfolio | 1–2 years | Quality bar across teams, leadership coaching |
| L6 Director | Cross-portfolio | 2–3 years | Long-term design vision, market differentiation |
| VP Product Design | Company | 3–5+ years | Design as competitive advantage, org strategy |

---

### `pm-lens`

Covers the Octopus Product Management career ladder.

| Level | Scope | Horizon | Primary focus |
|---|---|---|---|
| Product Manager | Team / single area | Cycle-based | Customer discovery, feature delivery, acceptance criteria |
| Senior PM | Cross-team | 6–12 months | Cross-team initiatives, hypothesis testing, stakeholder advocacy |
| Principal PM | Strategic / ambiguous | 12–18 months | New capabilities, market bets, validated strategic direction |
| Director of Product | Full portfolio | Multi-year | Product storyboard, market strategy, PM enablement |

---

### `eng-lens`

Covers the Octopus Engineering career ladder.

| Level | Scope | Horizon | Primary focus |
|---|---|---|---|
| L2 Software Engineer | Self / task | Current cycle | Complete defined work well, learn fast, escalate correctly |
| L3 Senior Engineer | Team | Current + next cycle | End-to-end feature ownership, mentoring, no gold-plating |
| L4 Lead Engineer | Team (5–15) | 6–12 months | Inception to production, architecture, task decomposition |
| L5 Principal Engineer | Group | 12+ months | Technical strategy, target architecture, team empowerment |

---

## Level detection

Each lens auto-detects the right level using five signal dimensions:

| Dimension | Lower levels | Higher levels |
|---|---|---|
| **Scope** | Team / squad / single feature | Portfolio / org-wide / company strategy |
| **Impact horizon** | This cycle / sprint | 12+ months / multi-year / vision |
| **Stakeholders** | Team-internal | RLT / ELT / board / market |
| **Complexity** | Well-defined, clear scope | Highly ambiguous, no precedent |
| **Work type** | Bug / component / feature | Platform / program / operating model |

The skill states the detected level, a confidence rating (High / Medium / Low), and the 2–3 strongest signals driving the conclusion.

---

## What you get back

Every lens returns the same five-part output, calibrated to the detected level:

```
Level Detected: [Level name]
Confidence: High / Medium / Low
Key signals: ...

Questions this level would ask:
  [3–5 specific questions about the document content]

How to break down the work:
  [Concrete, ordered task and activity breakdown]

Dependencies and risks:
  [What could go wrong or needs input from others]

What "done" looks like at this level:
  [Level-appropriate success definition]

One thing this level would push back on:
  [The single most important challenge or reframe]
```

---

## File structure

```
role-lenses/
├── README.md                   ← This file
├── HOW-TO-USE.md               ← Installation and usage guide
│
├── design-lens/
│   └── SKILL.md
│
├── pm-lens/
│   └── SKILL.md
│
└── eng-lens/
    └── SKILL.md
```

---

## Based on

- Octopus Deploy Product Design career framework (2025 refresh) — L3 through VP
- Octopus Deploy Engineering career framework — L2 through L5 Principal
- Octopus Deploy Product Management career framework — PM through Director of Product
