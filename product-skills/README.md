# Product Skills Suite

Three AI advisor skills for Product Strategy, Product Management, and Product Design — built
on industry best practice standards with structured checkpoints at every stage of product work.

---

## What These Skills Do

Each skill acts as a specialist advisor that knows **when to ask questions**, not just how to
analyse documents. Every skill operates in four modes:

| Mode | When to use |
|---|---|
| **Kick-off** | Starting a phase of work — aligns the team, surfaces assumptions, confirms prerequisites |
| **Check-in** | Mid-work — evaluates quality against benchmarks, finds gaps before they compound |
| **Handover** | End of phase — runs the quality gate, checks all deliverables, blocks low-quality transfers |
| **Analysis** | Deep review — full structured assessment of a document or artefact against best practice |

**They work from whatever you share.** Paste text, upload a file, describe your work, or share
a link. No integrations or specific tools required.

---

## The Three Skills

### Product Strategy (`product-strategy`)

**Primary concern**: Is this the right thing to build, and is the case for building it now well-reasoned?

Runs structured checkpoints at:
- **Kick-off**: 15 questions across strategic context, goal, constraints, assumptions, and alignment
- **Check-in**: Evidence quality, opportunity framing, direction reasoning, open questions
- **Handover (to PM)**: 12-point completeness check + 9-deliverable scorecard with MQB gate

Key outputs: strategic clarity audit, drafted goal/problem/why-now, signal quality assessment,
insight→direction chain trace, 2D assumption map, gap register, 5 strategic directions.

**Minimum Quality Bar for PS→PM handover**: Goal + Problem statement + Why now + Scope boundaries must all be present.

---

### Product Manager (`product-manager`)

**Primary concern**: Is the problem validated, is scope right for this stage, and does design have everything it needs?

Runs structured checkpoints at:
- **Kick-off**: 16 questions across problem alignment, discovery planning, constraints, and stakeholders
- **Check-in**: Discovery quality, insight formation, requirement completeness, design readiness
- **Handover (to PD)**: 13-point completeness check + 10-deliverable scorecard with MQB gate
- **Handover (to Eng)**: Spec completeness, requirements traceability, acceptance criteria

Key outputs: scope assessment, signal audit, clarity audit with drafted elements, needs and
requirements register, discovery quality review, insight chain trace, assumption map, gap register,
5 PM directions.

**Minimum Quality Bar for PM→PD handover**: Problem statement + User needs + Success metrics + V1 scope + Known constraints must all be present.

---

### Product Designer (`product-designer`)

**Primary concern**: Is the design grounded in the right problem, at the right fidelity, and ready for what comes next?

Runs structured checkpoints at:
- **Kick-off**: 13 questions across problem understanding, scope, fidelity, constraints, and validation
- **Check-in**: Design grounding, flow completeness, fidelity, system consistency, assumptions
- **Handover (to Eng)**: 15-point completeness check + 9-deliverable scorecard with MQB gate
- **Handover (Stakeholder sign-off)**: 7-point presentation quality check

Key outputs: fidelity assessment, flow completeness audit, design thinking rigour check,
design system alignment, clarity audit, assumption map, gap register, engineering readiness
check, 5 design directions.

**Minimum Quality Bar for PD→Eng handover**: All screen states + user flows (happy + error + empty) + annotations + component spec + accessibility basics must be complete.

---

## How the Skills Work Together

The three skills form a quality chain. Each skill can detect when an adjacent skill is needed
and recommend escalation.

```
                    ┌─────────────────┐
                    │  Product        │
                    │  Strategy       │
                    │                 │
                    │  Is this right? │
                    │  Why now?       │
                    └────────┬────────┘
                             │ Handover: Goal, Problem, Why now,
                             │ Strategic context, Assumptions
                             ▼
                    ┌─────────────────┐
                    │  Product        │
                    │  Manager        │
                    │                 │
                    │  Right problem? │
                    │  Right scope?   │
                    └────────┬────────┘
                             │ Handover: Problem statement, User needs,
                             │ Success metrics, Scope, Constraints, Research
                             ▼
                    ┌─────────────────┐
                    │  Product        │
                    │  Designer       │
                    │                 │
                    │  Right design?  │
                    │  Right fidelity?│
                    └────────┬────────┘
                             │ Handover: All states, Flows,
                             │ Annotations, Component spec, A11y
                             ▼
                         Engineering
```

**Escalation logic**: Issues at a lower layer block higher-layer work.
- Strategic gaps (wrong problem, no 'why now') → block PM and PD work
- PM gaps (no requirements, unvalidated problem) → block detailed design
- Design gaps (incomplete flows, missing states) → block engineering handoff

---

## Quality Framework

All three skills share the same reference standards:

### Signal Quality Tiers

| Tier | Type | Weight |
|---|---|---|
| 1 | Observed behaviour, quantitative data | Highest |
| 2 | Qualitative user research | High |
| 3 | Synthesised inference, competitive analysis | Medium |
| 4 | Expert judgement | Low-medium |
| 5 | Unvalidated internal opinion | Low |
| 6 | Untested assumption | Treat as risk |

### Insight → Direction Chain

Every product direction should be traceable through five links:
```
Raw signal → Insight → Opportunity → Direction → Decision
```

### Assumption Map (2×2)

Assumptions are mapped on importance (y-axis) vs evidence strength (x-axis).
The top-right quadrant (Important + Weak evidence) is the critical validation priority.

### Stage Model

| Stage | Purpose | Appropriate output |
|---|---|---|
| Explore | Understand the problem | Research, opportunity framing |
| Define | Frame the problem | Problem statement, goals, requirements |
| Design | Solve the problem | Flows, wireframes, prototypes |
| Deliver | Build the solution | Specs, edge cases, handoff |
| Learn | Measure and improve | Metrics, findings, iteration |

---

## File Structure

```
product-skills/
├── README.md                              ← This file
├── SETUP.md                               ← Installation and usage
│
├── shared/
│   ├── industry-standards.md             ← Frameworks and best practice reference
│   ├── quality-standards.md              ← Benchmarks, MQBs, and deliverable checklists
│   └── checkpoint-questions.md           ← Full question banks per role and checkpoint
│
├── product-strategy/
│   ├── SKILL.md                           ← Product Strategy skill
│   └── references/
│       ├── industry-standards.md
│       ├── quality-standards.md
│       └── checkpoint-questions.md
│
├── product-manager/
│   ├── SKILL.md                           ← Product Manager skill
│   └── references/
│       ├── industry-standards.md
│       ├── quality-standards.md
│       └── checkpoint-questions.md
│
└── product-designer/
    ├── SKILL.md                           ← Product Designer skill
    └── references/
        ├── industry-standards.md
        ├── quality-standards.md
        └── checkpoint-questions.md
```

---

## What These Skills Are Not

- **Not a replacement for human judgement.** They surface issues and draft candidate answers — the team decides.
- **Not a compliance checklist.** Not every element applies to every piece of work. The skills identify what matters most at the current stage.
- **Not prescriptive about process.** They work with any methodology: Shape Up, Scrum, dual-track agile, continuous discovery, or a custom approach.
- **Not an audit tool for blame.** The goal is to surface gaps early enough to fix them — not to score people after the fact.
