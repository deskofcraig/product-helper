# Product designer agent system

A complete set of agentic AI files for product designers. Nine
specialist agents plus an orchestrator, all sharing a common
self-improvement protocol that lets them get better over time —
without becoming biased toward any specific project or feature.

---

## How to use these files

Each agent lives in its own folder. To activate an agent:

1. Open a new Claude Project (or equivalent AI tool that supports
   system prompts)
2. Paste the contents of the agent's `system-prompt.md` into the
   system prompt
3. Paste the contents of the agent's `persona.md` after the system
   prompt
4. Paste the contents of `_shared/context.md` after the persona
5. Start the conversation

For multi-agent workflows, use the **orchestrator** as your starting
point and describe your goal — it will sequence the right agents.

---

## Agent directory

| Agent | Folder | Job |
|---|---|---|
| Orchestrator | `orchestrator/` | Coordinates all agents toward your goal |
| Project planner | `project-planner/` | Generates a tailored task plan from your kick-off template |
| Continuous discovery | `continuous-discovery/` | Frames opportunities, maps assumptions, plans discovery (Teresa Torres methodology) |
| Competitive research | `competitive-research/` | Researches how competitors approach a feature |
| User research | `user-research/` | Synthesises interviews, surveys, session notes |
| Insight synthesis | `insight-synthesis/` | Turns research into prioritised design insights |
| Design brief | `design-brief/` | Produces a clear brief from insights |
| Variations | `variations/` | Generates distinct design directions |
| Design system audit | `design-system-audit/` | Audits designs for system consistency |
| Copy & microcopy | `copy-microcopy/` | Writes all in-product copy |
| Accessibility audit | `accessibility-audit/` | Audits against WCAG AA |
| Handoff | `handoff/` | Produces engineering-ready specifications |
| Design QA | `design-qa/` | Compares built UI against original designs |

---

## Standard pipelines

### Project kick-off (any new project)
```
Fill in project-kickoff-template.md
        ↓
Project planner agent
        ↓
Continuous discovery agent
        ↓
Competitive research agent  +  User research agent
        ↓
Insight synthesis agent
        ↓
Design brief agent
```

### Discovery → brief
```
Competitive research agent
User research agent
        ↓
Insight synthesis agent
        ↓
Design brief agent
```

### Creation
```
Design brief agent
        ↓
Variations agent  +  Copy & microcopy agent
```

### Pre-launch quality
```
Design system audit  +  Accessibility audit
        ↓
Handoff agent
        ↓
Design QA agent
```

---

## File structure (per agent)

```
/agents/
  _shared/
    context.md                   ← YOUR product/project context (fill this in)
    self-improvement-protocol.md ← How agents log and refine themselves

  [agent-name]/
    system-prompt.md             ← What the agent does and how
    persona.md                   ← How it thinks and communicates
    learning-log.md              ← Updated by the agent after tasks
    proposed-update.md           ← Created by agent when it has a refinement
                                    suggestion (delete after review)
```

---

## The self-improvement system

Every agent is instructed to evaluate its own output after each task
and log what worked, what didn't, and — when a pattern repeats —
propose a concrete change to its own files.

**The loop:**
1. Agent completes a task
2. Agent appends an entry to its `learning-log.md`
3. If a problem has occurred 2+ times, agent creates `proposed-update.md`
4. You review and decide: accept, reject, or modify
5. Approved changes get copied into `system-prompt.md` or `persona.md`
6. `proposed-update.md` is deleted

**The anti-drift guarantee:**
Agents are instructed that all proposed refinements must be
project-agnostic — testable on any job in any domain. Any refinement
that references a specific company, product, or feature by name is
invalid. This keeps agents sharp without making them narrow.

---

## Customising for your context

The only file you need to fill in is `_shared/context.md`. This tells
every agent:
- What your product is and who your users are
- Your design system and brand voice
- Platform constraints
- What you've already researched

Update it whenever your product or constraints change. You don't need
to update individual agent files — they all pull from this shared
context.

---

## Tips

- **Start with the orchestrator** for any multi-step task. Describe
  your goal in plain language and let it route the work.
- **Run agents individually** when you have a single, specific job —
  e.g. "just audit these screens for accessibility."
- **Read the learning logs** occasionally. They're the cheapest form
  of process improvement available.
- **Protect your judgment.** These agents handle volume and structure.
  You own taste, strategy, and the decisions that define the product.
