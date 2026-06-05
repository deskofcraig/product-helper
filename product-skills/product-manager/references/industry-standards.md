# Industry Best Practice Standards Reference

This document defines the frameworks, standards, and evaluation criteria used across all three
product skills. It is tool-agnostic and role-neutral — these standards apply regardless of what
software, methodology, or process the team uses.

---

## 1. Product Development Stages

All work exists at one of these stages. Stage determines what is appropriate to produce and evaluate.

| Stage | Purpose | Appropriate Output | Common Mistake |
|---|---|---|---|
| **Explore** | Understand the problem space | Research notes, user quotes, opportunity framing, HMW questions | Jumping to solutions |
| **Define** | Frame the problem and set direction | Problem statement, goal, success metrics, hypotheses, requirements | Vague or solution-shaped problems |
| **Design** | Explore and validate solutions | Flows, wireframes, prototypes, interaction models | Skipping validation, wrong fidelity |
| **Deliver** | Build and ship | Specs, edge cases, QA criteria, handoff documentation | Missing states, ambiguous specs |
| **Learn** | Measure and improve | Metrics review, usability findings, iteration backlog | Skipping learning entirely |

**Fidelity within Design stage:**

| Fidelity | Purpose | Characteristics |
|---|---|---|
| Conceptual sketch | Explore ideas quickly | Rough, disposable, no detail |
| Lo-fi wireframe | Structure and flow | Layout only, no visual design, annotated |
| Mid-fi wireframe | Interaction and hierarchy | Key components, spacing, states emerging |
| Hi-fi mockup | Visual design + interactions | Design system applied, all key states |
| Prototype | Test with users | Clickable/interactive, specific scenarios only |
| Production spec | Engineering handoff | Every state, every edge case, exact measurements, tokens |

---

## 2. Core Clarity Elements

Every piece of product work should be able to answer these four questions. Absence of any one is
a gap that should be surfaced.

### 2.1 Goal
What outcome are we trying to achieve?

A strong goal is:
- Outcome-oriented (not output or activity)
- Measurable or at least verifiable
- Time-bounded where possible
- Distinct from the solution

**Weak**: "Build a new dashboard"
**Strong**: "Reduce time-to-first-insight for new users by 40% within 3 months of launch"

### 2.2 Problem Statement
What specific problem does this work address, and for whom?

A strong problem statement:
- Names the user or stakeholder experiencing the problem
- Describes what they are trying to do
- Identifies the barrier, friction, or gap
- States the impact of the problem going unsolved
- Does NOT contain a solution

Template: *"[User] is trying to [job/goal] but [barrier/friction], which means [impact]."*

**Weak**: "Users need a better search experience"
**Strong**: "Returning customers trying to reorder past purchases can't find their order history without contacting support, which creates unnecessary support load and erodes trust"

### 2.3 Why Now
What makes this the right moment to solve this problem?

A strong Why Now includes at least one of:
- **Urgency signal**: something has changed that makes this more pressing (competitor move, regulation, user behaviour shift, data spike)
- **Strategic window**: alignment with a company goal, funding cycle, or platform change that makes this the optimal moment
- **Cost of delay**: what gets worse or more expensive if this is not addressed now
- **Enabling condition**: something that recently became possible (new capability, new data, new hire, cleared dependency)

**Weak**: "It's been requested a few times"
**Strong**: "Support tickets for this issue have grown 60% in 90 days following the new user onboarding change, and the Q3 retention goal makes this directly relevant now"

### 2.4 Needs & Requirements
What must be true for this work to succeed?

Distinguish between:
- **User needs**: what users are trying to accomplish (JTBD framing preferred)
- **Business requirements**: constraints or outcomes the business needs
- **Technical constraints**: platform, performance, security, compatibility limits
- **Design requirements**: accessibility, internationalisation, responsive contexts
- **Out-of-scope**: what is explicitly not being addressed in this iteration

---

## 3. Signal Quality Framework

Not all inputs to product work carry equal weight. Evaluate signal quality against this scale.

| Signal Tier | Type | Examples | Weight |
|---|---|---|---|
| **Tier 1 — Empirical** | Observed behaviour, quantitative data | Analytics, A/B test results, task completion rates, error logs | Highest |
| **Tier 2 — Direct user evidence** | Qualitative research with users | Interview quotes, usability test recordings, surveys with open responses | High |
| **Tier 3 — Structured inference** | Synthesised from multiple data points | Insight from research synthesis, competitive analysis, market data | Medium |
| **Tier 4 — Expert judgement** | Reasoned from experience | Product instinct, domain expertise, analogous markets | Low-medium |
| **Tier 5 — Unvalidated opinion** | Stated without evidence | "Users will love this", "It would be great if", stakeholder preference | Low |
| **Tier 6 — Assumption** | Believed true, not checked | "Everyone knows that…", "Obviously users want…" | Treat as risk |

**Red flags**: work driven primarily by Tier 5–6 signals; Tier 1–2 signals that are old (>12 months); signals cherry-picked to support a predetermined direction.

---

## 4. Insight → Direction Chain

Every product direction should be traceable back to evidence. The chain has five links:

```
Raw signal  →  Insight  →  Opportunity  →  Direction  →  Decision
```

| Link | Definition | Example |
|---|---|---|
| **Raw signal** | Something observed, measured, or heard | "62% of users abandon the form on step 3" |
| **Insight** | What the signal means | "Users don't understand what information is required at step 3 and why" |
| **Opportunity** | What could be improved | "Reduce confusion at step 3 by improving field clarity and progressive disclosure" |
| **Direction** | The chosen response | "Redesign the step 3 form to clarify required fields and add inline guidance" |
| **Decision** | The specific, bounded choice | "For V1: rewrite field labels and add tooltip help; defer full flow restructure to V2" |

**Common chain breaks:**
- Signal → Direction (skipped insight and opportunity — solution-first thinking)
- Insight → Decision (skipped direction — no evaluation of alternatives)
- Direction stated with no traceable signal (pure opinion driving work)

---

## 5. Assumption Mapping (2×2)

Assumptions are beliefs the work depends on that have not yet been validated. All work carries
assumptions — the goal is to make them explicit and prioritise which to validate first.

**Axes:**
- **Y-axis**: Importance — how critical is this assumption to the work succeeding?
- **X-axis**: Evidence strength — how much supporting evidence currently exists?

```
  MORE
IMPORTANT
    │
    │  [Confirmed foundations]  │  [CRITICAL — validate first]
    │  Important + Strong       │  Important + Weak
    │  evidence                 │  evidence
    │                           │
────┼───────────────────────────┼────
    │                           │
    │  [Monitor / low priority] │  [Deprioritise]
    │  Less important + Strong  │  Less important + Weak
    │  evidence                 │  evidence
    │                           │
  LESS                     ←   →
IMPORTANT              WEAK    STRONG
                      EVIDENCE EVIDENCE
```

**Quadrant actions:**
- **Top-right (Important + Weak evidence)**: These are your riskiest bets. Validate before investing further.
- **Top-left (Important + Strong evidence)**: Foundations to build on confidently.
- **Bottom-left (Less important + Strong evidence)**: Useful context, low urgency.
- **Bottom-right (Less important + Weak evidence)**: Deprioritise. Don't invest in validating.

**Common assumption categories:**
- *Desirability*: Users want this / will value this
- *Usability*: Users will understand and be able to use this
- *Feasibility*: We can build this within acceptable constraints
- *Viability*: This will work as a business / product decision
- *Adoptability*: Users will change their behaviour to use this

---

## 6. Stage-Appropriate Scope

A scope problem occurs when the detail or ambition of the work does not match the current stage.

**Over-scoped for stage** (too much detail too early):
- High-fi mockups when the problem hasn't been validated
- Detailed technical spec before requirements are locked
- Comprehensive design system before core flows are proven
- Full feature scope in a discovery document

**Under-scoped for stage** (missing fundamentals):
- Wireframes with no problem statement
- Discovery work with no user evidence
- Strategy document with no measurable goal
- Design spec with missing states and edge cases

---

## 7. Product Discovery Best Practices

Discovery is the process of identifying and validating problems worth solving.

Good discovery:
- Starts with the problem, not the solution
- Separates understanding (research) from ideation (design)
- Tests assumptions with the smallest possible experiment
- Involves users as frequently as feasible
- Produces insights, not just data
- Explicitly documents what was learned AND what it means

Weak discovery:
- Consists of internal workshops only
- Uses surveys without follow-up qualitative research
- Presents research findings without synthesis or interpretation
- Leads directly to a feature spec without opportunity framing
- Uses user quotes to validate a predetermined idea

---

## 8. Design Thinking Principles

Applied to product work, design thinking requires:

1. **Empathy before solution**: Understand real user context before designing responses
2. **Problem framing before solution framing**: A well-defined problem is already half-solved
3. **Diverge before converging**: Explore multiple options before committing
4. **Prototype to learn, not to confirm**: Prototypes should test assumptions, not showcase polish
5. **Test with real users**: Internal critique is useful; user testing is essential
6. **Iterate based on learning**: Incorporate what you learn, don't just ship what you built

---

## 9. Five Directions Format

When providing directional recommendations, use this format for clarity and actionability:

```
Direction [N]: [Action verb] + [specific focus area]
Signal:        [What evidence or observation supports this direction]
Because:       [The reasoning — what problem does this address or what opportunity does it unlock]
Owner:         [Product Strategy / Product Manager / Product Designer / Shared]
Urgency:       [Immediate / Near-term / Later]
```

Directions should be:
- Specific enough to act on
- Grounded in an observable signal or gap
- Owned by a clear role
- Distinct from each other (avoid directional overlap)

---

## 10. Skill Selection Logic

When work is presented, select the primary lens based on its dominant concern:

| If the primary question is about… | Lead skill |
|---|---|
| Is this the right thing to build? / Why now? / Strategic fit? | **Product Strategy** |
| Is the problem validated? / Is scope right? / What are the requirements? | **Product Manager** |
| Does this design solve the problem? / Is the flow right? / Is the fidelity appropriate? | **Product Designer** |

**Multi-lens mode**: Work that spans multiple concerns should be reviewed under all relevant lenses.
Each skill section should be clearly labelled and can be read independently.

**Escalation order**: If foundational issues are found, address them first before higher-order ones.
- Strategy issues (wrong problem, wrong time) → block PM and PD work
- PM issues (no requirements, wrong scope) → block PD detailed work
- PD issues (wrong fidelity, incomplete flows) → block engineering handoff
