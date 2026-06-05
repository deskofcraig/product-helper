# product-skills

Three specialist advisor skills for Product Strategy, Product Management, and Product Design — grounded in industry best practice, with structured quality gates at every stage of product work.

---

## What this suite does

Each skill acts as a discipline-specific advisor that asks the right questions at the right time. The skills don't just analyse documents after the fact — they run structured checkpoints at kick-offs, during work, and at handover, enforcing Minimum Quality Bars (MQBs) before anything moves to the next stage.

**The chain:**

```
Product Strategy  →  Product Manager  →  Product Designer  →  Engineering
      ↓                    ↓                    ↓
   MQB gate             MQB gate             MQB gate
```

Issues at an earlier stage block later stages. Strategic gaps block PM work. PM gaps block design. Design gaps block engineering handoff.

---

## The three skills

### `product-strategy`

**Primary concern:** Is this the right thing to build, and is the case for building it now well-reasoned?

Covers: opportunity framing, strategic context, goal setting, assumptions, signal quality, 'why now', direction reasoning.

**Minimum Quality Bar for handover to PM:**
Goal + Problem statement + Why now + Scope boundaries must all be present.

---

### `product-manager`

**Primary concern:** Is the problem validated, is scope right for this stage, and does design have everything it needs?

Covers: problem alignment, discovery planning, research quality, insight formation, requirements, acceptance criteria, design readiness.

**Minimum Quality Bar for handover to Design:**
Problem statement + User needs + Success metrics + V1 scope + Known constraints must all be present.

---

### `product-designer`

**Primary concern:** Is the design grounded in the right problem, at the right fidelity, and ready for what comes next?

Covers: problem grounding, flow completeness, fidelity appropriateness, design system alignment, accessibility, engineering readiness.

**Minimum Quality Bar for handover to Engineering:**
All screen states + User flows (happy + error + empty) + Annotations + Component spec + Accessibility basics must be complete.

---

## The four modes

Every skill operates in four modes. The skill detects which mode applies from what you share.

| Mode | When it applies | What it does |
|---|---|---|
| **Kick-off** | Starting a phase of work | Asks structured questions, surfaces assumptions, confirms prerequisites before work begins |
| **Check-in** | Mid-work review | Evaluates quality against benchmarks, identifies gaps before they compound |
| **Handover** | End of phase, passing to the next function | Runs the MQB gate, checks all deliverables, blocks low-quality transfers |
| **Analysis** | Deep review of a complete document | Full structured assessment against best practice benchmarks |

---

## Quality framework

All three skills share the same reference standards in `shared/`.

### Signal quality tiers

| Tier | Type | Weight |
|---|---|---|
| 1 | Observed behaviour, quantitative data | Highest |
| 2 | Qualitative user research | High |
| 3 | Synthesised inference, competitive analysis | Medium |
| 4 | Expert judgement | Low-medium |
| 5 | Unvalidated internal opinion | Low |
| 6 | Untested assumption | Treat as risk |

### Insight → Direction chain

Every product direction should be traceable through five links:

```
Raw signal → Insight → Opportunity → Direction → Decision
```

### Stage model

| Stage | Purpose | Appropriate output |
|---|---|---|
| Explore | Understand the problem | Research, opportunity framing |
| Define | Frame the problem | Problem statement, goals, requirements |
| Design | Solve the problem | Flows, wireframes, prototypes |
| Deliver | Build the solution | Specs, edge cases, handoff |
| Learn | Measure and improve | Metrics, findings, iteration |

---

## File structure

```
product-skills/
├── README.md                              ← This file
├── HOW-TO-USE.md                          ← Installation and usage guide
│
├── shared/
│   ├── industry-standards.md             ← Frameworks and best practice reference
│   ├── quality-standards.md              ← Benchmarks, MQBs, and deliverable checklists
│   └── checkpoint-questions.md           ← Full question banks per role and checkpoint
│
├── product-strategy/
│   ├── SKILL.md
│   ├── TASKS.md
│   └── references/
│       ├── industry-standards.md
│       ├── quality-standards.md
│       └── checkpoint-questions.md
│
├── product-manager/
│   ├── SKILL.md
│   ├── TASKS.md
│   └── references/
│       ├── industry-standards.md
│       ├── quality-standards.md
│       └── checkpoint-questions.md
│
└── product-designer/
    ├── SKILL.md
    ├── TASKS.md
    └── references/
        ├── industry-standards.md
        ├── quality-standards.md
        └── checkpoint-questions.md
```

---

## What these skills are not

**Not a replacement for human judgement.** They surface issues and draft candidate answers — the team decides.

**Not a compliance checklist.** Not every element applies to every piece of work. The skills identify what matters most at the current stage.

**Not prescriptive about process.** They work with any methodology: Shape Up, Scrum, dual-track agile, continuous discovery, or a custom approach.

**Not an audit tool for blame.** The goal is to surface gaps early enough to fix them — not to score people after the fact.
