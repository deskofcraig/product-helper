# product-advisor

The orchestrating skill for the Product Helper suite. It knows both sub-suites — `product-skills` and `role-lenses` — and routes intelligently between them based on what you share and what you need.

---

## What it does

`product-advisor` is the single entry point when you want a complete or cross-functional read of any work document. Rather than requiring you to know which sub-skill to invoke, it reads your document, identifies where the work sits in the product chain, and determines the right combination of analysis to run.

**The two suites it coordinates:**

| Suite | Folder | Primary question |
|---|---|---|
| `product-skills` | `../product-skills/` | Is this work done correctly for its stage? |
| `role-lenses` | `../role-lenses/` | Is this being thought about at the right level of scope and ambition? |

Running both on the same document gives you a complete picture that neither suite provides alone: whether the work is quality-complete for its stage, *and* whether it's scope-appropriate for the level of person doing it.

---

## The five routes

`product-advisor` selects one of five routes based on what you share:

### Route A — Process quality only
For kick-offs, check-ins, handover gates, and deep quality analysis. Delegates to the relevant `product-skills` skill and mode.

*Use when:* You want structured checkpoint questions, an MQB gate, or a benchmark assessment.

### Route B — Seniority perspective only
For level detection and persona-based task breakdown. Delegates to the relevant `role-lenses` skill.

*Use when:* You want to know if you're thinking at the right scope, or what a more senior view would add.

### Route C — Full combined review
Runs both suites in sequence, then synthesises the findings — showing where the two analyses agree and where they add to each other.

*Use when:* You want the most complete picture of a document or piece of work.

### Route D — Routing guidance
Identifies which specific sub-skill and mode is most relevant to your situation.

*Use when:* You're unsure where to start, or want a recommendation before going deeper.

### Route E — Cross-functional review
Runs all three role-lenses (Design, PM, Engineering) against the same document and produces a consolidated cross-discipline view.

*Use when:* A document has cross-functional implications and you want to see where disciplines agree, diverge, and what the handover chain looks like.

---

## How it knows what to do

`product-advisor` reads four dimensions of your document before routing:

**Stage in the chain** — Where does this sit?
```
Strategy → Product Management → Product Design → Engineering
```

**Mode** — What kind of checkpoint is needed?
Kick-off / Check-in / Handover / Analysis / Full review / Routing

**Discipline(s)** — Which functions are in scope?
Design, PM, Engineering, or all three

**Seniority signals** — What level does the work appear to be operating at?
Scope, impact horizon, stakeholders, complexity, work type

---

## What it references

`product-advisor` reads from adjacent folders when running its analysis:

```
product-helper/
├── product-advisor/          ← lives here
│   └── SKILL.md
│
├── product-skills/           ← reads from here for process quality
│   ├── product-strategy/SKILL.md
│   ├── product-manager/SKILL.md
│   ├── product-designer/SKILL.md
│   └── shared/
│       ├── quality-standards.md
│       ├── industry-standards.md
│       └── checkpoint-questions.md
│
└── role-lenses/              ← reads from here for seniority perspective
    ├── design-lens/SKILL.md
    ├── pm-lens/SKILL.md
    └── eng-lens/SKILL.md
```

This folder structure must be kept intact for `product-advisor` to work correctly.

---

## Output

Every response from `product-advisor` ends with a **recommended next skill** — the specific sub-skill and mode to go to for deeper work, with a one-line rationale. It never leaves you without a clear next step.
