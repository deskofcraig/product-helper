# Product Helper

A suite of Claude skills for Octopus product teams — combining process quality gates with role-appropriate thinking across Design, Product Management, and Engineering.

---

## What's in this folder

```
product-helper/
├── README.md                        ← You are here
├── HOW-TO-USE.md                    ← Installation and usage guide
│
├── product-advisor/                 ← Orchestrating skill (start here)
│   └── SKILL.md
│
├── product-skills/                  ← Process quality suite
│   ├── README.md
│   ├── HOW-TO-USE.md
│   ├── product-strategy/
│   ├── product-manager/
│   ├── product-designer/
│   └── shared/
│
└── role-lenses/                     ← Seniority perspective suite
    ├── README.md
    ├── HOW-TO-USE.md
    ├── design-lens/
    ├── pm-lens/
    └── eng-lens/
```

---

## The three components

### product-advisor

The orchestrating skill. It knows about both suites below and routes intelligently between them based on what you share. Start here when you're unsure which skill to use, want a full review, or need a cross-functional read of a document.

**Invoke with:** `product-advisor`

---

### product-skills

A process quality suite with three specialist advisor skills — one each for Product Strategy, Product Management, and Product Design. Each skill operates across four modes (kick-off, check-in, handover, analysis) and enforces Minimum Quality Bar gates at each stage transition.

**The chain it covers:**

```
Product Strategy → Product Manager → Product Designer → Engineering
```

**Invoke with:** `product-strategy`, `product-manager`, or `product-designer`

See `product-skills/README.md` for full details.

---

### role-lenses

A seniority perspective suite with three lenses — one each for Design, PM, and Engineering. Each lens auto-detects the appropriate career level from your document and applies that level's mindset, questions, task breakdown, and risks.

**The levels it covers:**

| Lens | Levels |
|---|---|
| `design-lens` | L3 Senior → L4 Lead → L5 Principal → L5 Assoc Director → L6 Director → VP |
| `pm-lens` | PM → Senior PM → Principal PM → Director |
| `eng-lens` | L2 → L3 Senior → L4 Lead → L5 Principal |

**Invoke with:** `design-lens`, `pm-lens`, or `eng-lens`

See `role-lenses/README.md` for full details.

---

## How the two suites complement each other

| Suite | Primary question | When to reach for it |
|---|---|---|
| `product-skills` | Is this work done correctly for its stage? | Kick-offs, check-ins, handovers, quality gates, MQB checks |
| `role-lenses` | Is this being thought about at the right level of scope and ambition? | Sanity-checking your framing, understanding what a more senior view would add, calibrating before a stakeholder conversation |

Running both on the same document gives you a complete picture: whether the work is quality-complete for its stage, and whether it's scope-appropriate for the level involved.

`product-advisor` handles the combination automatically.

---

## Based on

- Octopus Deploy Product Design career framework (2025 refresh) — L3 through VP
- Octopus Deploy Engineering career framework — L2 through L5 Principal
- Octopus Deploy Product Management career framework — PM through Director
- Industry best practice standards for product strategy, discovery, and design quality
