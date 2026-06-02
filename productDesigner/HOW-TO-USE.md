# Product designer agent system — setup and usage guide

A practical guide to getting your agent system running and using it
confidently day-to-day. No technical background required.

---

## Table of contents

1. [What this system is](#1-what-this-system-is)
2. [Before you start — what you need](#2-before-you-start--what-you-need)
3. [Setup: step-by-step](#3-setup-step-by-step)
   - 3.1 [Fill in your context file](#31-fill-in-your-context-file)
   - 3.2 [Create a Project in Claude](#32-create-a-project-in-claude)
   - 3.3 [Set up the orchestrator](#33-set-up-the-orchestrator)
   - 3.4 [Set up each specialist agent](#34-set-up-each-specialist-agent)
4. [Understanding the file structure](#4-understanding-the-file-structure)
5. [How to use the agents](#5-how-to-use-the-agents)
   - 5.1 [The golden rule: start with the orchestrator](#51-the-golden-rule-start-with-the-orchestrator)
   - 5.2 [Running a single specialist agent](#52-running-a-single-specialist-agent)
   - 5.3 [Running a full pipeline](#53-running-a-full-pipeline)
6. [Agent reference: what each agent does](#6-agent-reference-what-each-agent-does)
7. [Common workflows with example prompts](#7-common-workflows-with-example-prompts)
   - 7.1 [I'm starting a new feature from scratch](#71-im-starting-a-new-feature-from-scratch)
   - 7.2 [I have user research and need a brief](#72-i-have-user-research-and-need-a-brief)
   - 7.3 [I need design options to react to](#73-i-need-design-options-to-react-to)
   - 7.4 [I need to audit my designs before handoff](#74-i-need-to-audit-my-designs-before-handoff)
   - 7.5 [I need to write all the copy for a flow](#75-i-need-to-write-all-the-copy-for-a-flow)
   - 7.6 [I need to QA what engineering built](#76-i-need-to-qa-what-engineering-built)
8. [The self-improvement system](#8-the-self-improvement-system)
   - 8.1 [How agents improve themselves](#81-how-agents-improve-themselves)
   - 8.2 [How to review and approve an update](#82-how-to-review-and-approve-an-update)
   - 8.3 [Maintaining your agents over time](#83-maintaining-your-agents-over-time)
9. [Tips for better outputs](#9-tips-for-better-outputs)
10. [Troubleshooting](#10-troubleshooting)
11. [Quick-start cheatsheet](#11-quick-start-cheatsheet)

---

## 1. What this system is

This is a set of text files that turn an AI tool (Claude) into a team
of specialist design assistants. Each assistant — called an agent —
has a specific job, a defined way of communicating, and the ability to
learn from its own work over time.

There are 11 agents in total:

- **1 orchestrator** — the one you talk to for big goals. It sequences
  and coordinates all the others.
- **10 specialist agents** — each expert in one part of the design
  workflow, from competitive research through to QA.

The agents don't replace your judgment. They handle the volume,
structure, and legwork so you can focus on the decisions that actually
require a designer's taste and experience.

---

## 2. Before you start — what you need

- A **Claude.ai account** (Pro or Team plan recommended — Projects are
  required, and these are available on paid plans)
- The **agent files** from this folder (you already have them)
- About **30 minutes** for initial setup
- A text editor to view and copy file contents (any will do — TextEdit,
  VS Code, Notion, anything)

You do not need to know how to code. These are plain text files.

---

## 3. Setup: step-by-step

### 3.1 Fill in your context file

The context file is the most important setup step. It gives every agent
the background knowledge they need so you never have to repeat yourself.

**File to edit:** `_shared/context.md`

Open it and fill in every section:

```
## Our product
Name: Workly
Category: SaaS productivity tool
Core use case: Helps small teams manage projects without the overhead
  of enterprise tools.
Current design stage: Redesigning the onboarding flow for v3.

## Our users
Primary audience: Non-technical team leads at companies of 5–50 people
Technical level: Non-technical
Key jobs to be done:
  - Set up a new project quickly without a learning curve
  - Assign tasks and see progress at a glance
  - Get their team up and running without training sessions

## Our design system
Tool: Figma
Component library: Custom — based loosely on Material but heavily
  modified. Components live in the "Workly DS" Figma library.
Brand voice: Warm, direct, slightly encouraging. Never corporate.
Accessibility standard: WCAG AA
...
```

Fill in every field honestly. Leave a field blank rather than guessing.
The agents work with what you give them.

**Save this file.** You will paste its contents into every agent's
system prompt during setup — and update it whenever your product
context changes.

---

### 3.2 Create a Project in Claude

Claude Projects let you give an AI a persistent system prompt — a set
of instructions that stay active across every conversation.

**Steps:**

1. Go to [claude.ai](https://claude.ai) and sign in
2. In the left sidebar, click **"New project"**
3. Name it clearly — e.g. "Design agents — [your product name]"
4. You will see a **"Project instructions"** field at the top of the
   project — this is where the system prompt goes

You will create one Project per agent. Each Project = one agent.

> **Why separate Projects?** Each agent needs to stay in its own lane.
> Mixing multiple agents into one Project causes them to blur their
> roles and produce worse outputs. Keep them separate.

---

### 3.3 Set up the orchestrator

Start here. The orchestrator is the agent you'll talk to most often.

**Steps:**

1. Create a new Project named **"Orchestrator"**
2. Open `orchestrator/system-prompt.md` in your text editor
3. Copy the entire contents
4. Open `orchestrator/persona.md`
5. Copy the entire contents and paste it directly after the system
   prompt (leave one blank line between them)
6. Open `_shared/context.md`
7. Copy the entire contents and paste it at the end (leave one blank
   line)
8. Save the Project instructions

Your orchestrator Project instructions should read:

```
[contents of system-prompt.md]

[contents of persona.md]

[contents of context.md]
```

That's it. The orchestrator is ready.

---

### 3.4 Set up each specialist agent

Repeat the same process for each of the 10 specialist agents. The
pattern is identical every time:

**For each agent folder (`competitive-research/`, `user-research/`,
`insight-synthesis/`, `design-brief/`, `variations/`,
`design-system-audit/`, `copy-microcopy/`, `accessibility-audit/`,
`handoff/`, `design-qa/`):**

1. Create a new Claude Project with the agent's name
2. Paste `system-prompt.md` contents into Project instructions
3. Paste `persona.md` contents after it (one blank line between)
4. Paste `_shared/context.md` contents after that (one blank line)
5. Save

**Estimated time per agent:** 3–5 minutes once you have the files open.
**Total time for all 11 agents:** approximately 30–40 minutes.

> **Tip:** Have the agent folders open in one window and Claude in
> another. Copy → switch window → paste → next agent. It goes quickly
> once you find a rhythm.

---

## 4. Understanding the file structure

```
agents/
│
├── HOW-TO-USE.md                 ← this file
├── README.md                     ← technical overview
│
├── _shared/
│   ├── context.md                ← YOUR product context (the only
│   │                                file you fill in)
│   └── self-improvement-protocol.md  ← how agents log and improve
│                                        themselves (don't edit this)
│
├── orchestrator/
│   ├── system-prompt.md          ← the agent's job description
│   ├── persona.md                ← how it thinks and communicates
│   └── learning-log.md           ← updated by the agent after tasks
│
├── competitive-research/
│   ├── system-prompt.md
│   ├── persona.md
│   └── learning-log.md
│
│   [... same structure for all 10 specialist agents]
│
└── [agent-name]/
    ├── system-prompt.md
    ├── persona.md
    ├── learning-log.md
    └── proposed-update.md        ← only appears when an agent has
                                     suggested a refinement to review
```

**The three file types explained:**

| File | What it is | Who writes it |
|---|---|---|
| `system-prompt.md` | The agent's job description — what it does, how it works, what it outputs | You (pre-written; you edit over time) |
| `persona.md` | The agent's communication style and thinking approach | You (pre-written; you edit over time) |
| `learning-log.md` | A running log of what the agent has learned from past tasks | The agent (appended after tasks) |
| `proposed-update.md` | A proposed change to its own files, for your review | The agent (created when a pattern recurs) |

---

## 5. How to use the agents

### 5.1 The golden rule: start with the orchestrator

For any goal that involves more than one step, open the **Orchestrator
Project** and describe what you want in plain language. You don't need
to know which agents to use or in what order — that's the orchestrator's
job.

**Example:**

> "I need to redesign our onboarding flow. We have three user
> interviews and I haven't done any competitive research yet.
> Where should we start?"

The orchestrator will identify which agents to run, in what order, and
what inputs each one needs. It will either run the tasks itself or give
you a clear sequence to follow.

---

### 5.2 Running a single specialist agent

When you have a specific, contained task — and you know which agent
handles it — go directly to that agent's Project.

**Example tasks suited to individual agents:**

- "Audit these 6 screens for accessibility issues" → Accessibility
  audit agent
- "Write the error messages for our payment flow" → Copy & microcopy
  agent
- "Check these designs against our design system" → Design system
  audit agent
- "Compare the built checkout screens against our Figma designs" →
  Design QA agent

**How to start the conversation:**

Open the agent's Project and give it everything it needs upfront:

1. The task description
2. The input material (paste text, describe screens, or share
   screenshots directly in Claude)
3. Any specific constraints or focus areas

**Example prompt for the accessibility audit agent:**

> "Please audit the attached screenshots of our onboarding flow
> (screens 1–6) against WCAG AA. Focus especially on colour contrast
> and keyboard navigation. Our users include people with low vision."

---

### 5.3 Running a full pipeline

For end-to-end work — from discovery through to handoff — the agents
are designed to feed into each other. The output of one becomes the
input of the next.

**The full pipeline in order:**

```
[Your goal / research question]
          ↓
  Competitive research agent    ←─── runs in parallel
  User research agent           ←─── runs in parallel
          ↓
  Insight synthesis agent
          ↓
  Design brief agent
          ↓
  Variations agent              ←─── runs in parallel
  Copy & microcopy agent        ←─── runs in parallel
          ↓
  Design system audit agent
  Accessibility audit agent
          ↓
  Handoff agent
          ↓
  Design QA agent
```

**In practice:**

You don't need to run all of these for every task. Run the agents
relevant to where you are in the process. The most common entry points:

- Starting from scratch → begin at competitive research + user research
- Have research, need direction → begin at insight synthesis
- Have a brief, need options → begin at variations
- Have designs, going to engineering → begin at system audit +
  accessibility audit
- Designs are built, need checking → go straight to design QA

---

## 6. Agent reference: what each agent does

### Orchestrator
**When to use:** Any multi-step goal, or when you're not sure which
agents you need.
**Give it:** A plain-language description of what you want to achieve.
**It returns:** A sequenced plan or complete multi-agent output, plus
a clear list of decisions you need to make.

---

### Competitive research agent
**When to use:** Before designing something, to understand how the
market solves a similar problem.
**Give it:** The feature area or flow to research. Optionally, named
competitors.
**It returns:** A structured teardown of how competitors approach the
area, cross-competitor patterns, differentiators, and design
implications.
**Does NOT do:** Make design recommendations.

---

### User research agent
**When to use:** When you have raw research material — interviews,
surveys, session notes, reviews — and need to extract meaning from it.
**Give it:** The research material (paste transcripts or notes
directly). The question the research is trying to answer.
**It returns:** Themed findings, representative verbatims, confidence
levels, contradictions, and suggested follow-up questions.
**Does NOT do:** Invent data or smooth over contradictions.

---

### Insight synthesis agent
**When to use:** After you have research outputs from one or both
discovery agents, and you need to turn them into design-relevant
insights.
**Give it:** Outputs from competitive research and/or user research.
The design question you're trying to answer.
**It returns:** Prioritised insights with evidence, the central tension
in the data, and what the evidence suggests (without making design
decisions).
**Does NOT do:** Propose design solutions.

---

### Design brief agent
**When to use:** When you're ready to define the design problem
formally before exploring solutions.
**Give it:** Insight synthesis output. Any business goals or constraints
not in the context file.
**It returns:** A structured brief with problem statement, design goal,
success criteria, hard and soft constraints, and what the brief
deliberately leaves open.
**Does NOT do:** Tell you what to design.

---

### Variations agent
**When to use:** When you have a brief and want real options to react
to, not a blank canvas.
**Give it:** The design brief. The component, screen, or flow to
generate variations for. The number of variations (default: 4).
**It returns:** Distinct design directions, each with a clear
description specific enough to sketch or prototype from, its trade-offs,
and a comparison table.
**Does NOT do:** Produce visual designs or choose a winner.

---

### Design system audit agent
**When to use:** Before handoff, or any time you want to check that
your designs are consistent with your design system.
**Give it:** Screenshots or descriptions of the designs to audit. A
description of your design system (or point to context.md).
**It returns:** A categorised list of inconsistencies — wrong, missing,
or ambiguous — with severity levels and recommended actions.
**Does NOT do:** Make aesthetic judgments without a system reference.

---

### Copy & microcopy agent
**When to use:** Any time you need to write or review the words in
your product — buttons, errors, empty states, tooltips, onboarding
copy, anything.
**Give it:** What needs to be written. The user's situation at the
moment they'll read it. Existing copy to review (if applicable).
**It returns:** 2–3 options per element, with brief rationale for
each, grounded in your product voice from context.md.
**Does NOT do:** Write marketing copy or finalise without giving you
options.

---

### Accessibility audit agent
**When to use:** Before handoff, or any time you want to check your
designs against WCAG standards.
**Give it:** Designs to audit (screenshots or descriptions). Target
standard (default: WCAG 2.1 AA).
**It returns:** Findings categorised by WCAG criterion and severity,
pattern analysis, accessibility positives, and specific fixes.
**Does NOT do:** Invent issues — every finding references a specific
criterion.

---

### Handoff agent
**When to use:** When designs are approved and you're preparing
specifications for engineering.
**Give it:** The screens, components, or flows to document. Your design
system details. The target engineering environment.
**It returns:** Component specifications with all variants and states,
spacing and typography tokens, interaction specifications, and a list
of engineering flags (ambiguities that need a decision before building).
**Does NOT do:** Make design decisions — it flags them for you.

---

### Design QA agent
**When to use:** After engineering has built your designs, to check
fidelity before launch.
**Give it:** Original designs (screenshots or Figma descriptions) and
the built product (screenshots or description of what was built).
**It returns:** A discrepancy log with severity levels, pattern
findings, accessibility regressions, and a list of engineering judgment
calls that need your review.
**Does NOT do:** Redesign or propose alternatives.

---

## 7. Common workflows with example prompts

### 7.1 I'm starting a new feature from scratch

**Agents involved:** Orchestrator → Competitive research → User
research → Insight synthesis → Design brief → Variations

**Open:** Orchestrator Project

**Prompt:**
> "I'm designing [feature name] for [product]. I have [X user
> interviews / no research yet / these session notes — paste them].
> I haven't done competitive research. I need to go from nothing to
> a design brief I can start exploring from. What's the best sequence
> and can you start the research?"

---

### 7.2 I have user research and need a brief

**Agents involved:** User research → Insight synthesis → Design brief

**Open:** User research agent Project

**Prompt:**
> "Here are the transcripts from 5 user interviews about our
> [feature/flow]. The question I was exploring: [your research
> question]. Please analyse these and give me the key findings."

Then take that output to the **Insight synthesis agent:**

> "Here are the findings from my user research [paste]. I also have
> this competitive research [paste or describe]. Please synthesise
> these into design insights for [the problem area]."

Then take the synthesis to the **Design brief agent:**

> "Here is the insight synthesis [paste]. Please turn this into a
> design brief for [feature/flow]."

---

### 7.3 I need design options to react to

**Agent:** Variations

**Open:** Variations agent Project

**Prompt:**
> "Here is my design brief [paste brief]. I need 4 variations for
> the [specific screen/component/flow]. The dimensions I care most
> about varying are: [e.g. how much we ask upfront vs. progressively,
> and whether the primary action is contextual or persistent]."

---

### 7.4 I need to audit my designs before handoff

**Agents involved:** Design system audit + Accessibility audit
(run both, then pass combined findings to Handoff)

**Open:** Design system audit agent Project

**Prompt:**
> "Please audit the attached screens [attach or describe] against
> our design system as described in my context. Focus on [spacing /
> typography / component usage / all of the above]. Flag anything
> that needs to be corrected before I hand off to engineering."

Then in the **Accessibility audit agent Project:**

> "Please audit the same screens [attach or describe] against WCAG
> 2.1 AA. Our users include [any relevant groups — e.g. older adults,
> colour blind users]."

---

### 7.5 I need to write all the copy for a flow

**Agent:** Copy & microcopy

**Open:** Copy & microcopy agent Project

**Prompt:**
> "I need copy for all the interactive elements in our [flow name].
> Here's the flow: [describe each screen and its purpose, or paste
> the screen names and what each one does].
>
> Key elements that need copy:
> - [Screen 1]: headline, subhead, primary CTA
> - [Screen 2]: form labels, helper text, error states
> - [Screen 3]: success state, next action
>
> Our voice is [brief description or point to context.md]."

---

### 7.6 I need to QA what engineering built

**Agent:** Design QA

**Open:** Design QA agent Project

**Prompt:**
> "I need to QA our [flow/screen name] before we launch.
>
> Here are the original approved designs: [paste screenshots or
> describe each screen in detail].
>
> Here is what engineering built: [paste screenshots of the
> implementation].
>
> Scope: [list what you want checked — e.g. all screens in the
> checkout flow, just the mobile breakpoint, just the error states]."

---

## 8. The self-improvement system

### 8.1 How agents improve themselves

Every agent is instructed to do a quick self-evaluation after each
task and ask: did my output actually work? Was my process efficient?
Was there a step I could do better?

When an agent notices something worth recording, it appends an entry
to its `learning-log.md`. When the same issue comes up twice or more,
it creates a `proposed-update.md` file containing a suggested change
to its own `system-prompt.md` or `persona.md`.

This is designed to happen quietly, in the background, without
requiring anything from you — until there's a proposed update to review.

**What a learning log entry looks like:**

```markdown
## 2025-08-14 — Task type: onboarding flow audit

### What worked well
The comparison table format made it very easy for the designer to
scan for patterns across competitors quickly.

### What didn't work
I structured findings by competitor first, then dimension — but the
designer needed them by dimension first to compare patterns. This
caused extra work on their end.

### Proposed refinement
Add a step to the process: ask the designer upfront whether they
want findings structured by competitor or by dimension. Default
to dimension-first unless competitor-first is specified.

### Confidence in refinement
Medium — this came up once but the failure was clear.
```

---

### 8.2 How to review and approve an update

When an agent creates a `proposed-update.md`, you'll find it in that
agent's folder alongside the other files.

**Review process:**

1. Open `proposed-update.md` and read the proposed change
2. Check: is this change project-agnostic? (Would it work equally
   well on any design project, not just the one that triggered it?)
3. If yes and you agree: copy the proposed change into the relevant
   file (`system-prompt.md` or `persona.md`)
4. Delete `proposed-update.md` from the folder
5. Open that agent's Project in Claude and update the system prompt
   to reflect the change

**If you disagree with the proposed change:**

- Delete `proposed-update.md`
- Optionally, add a note to `learning-log.md` explaining why the
  proposal was rejected (this helps the agent not repeat it)

**If the change is partially right:**

- Modify it before applying it — you are always in control of what
  the agent becomes

> **Important:** Never apply a proposed update that references a
> specific company, product name, or project. Updates must be
> general enough to improve the agent for all future work.

---

### 8.3 Maintaining your agents over time

A healthy agent system requires light, regular maintenance — similar
to keeping a wiki or documentation up to date.

**When to update `_shared/context.md`:**
- You move to a new product or project
- Your design system changes significantly
- Your target users or platforms change
- You've completed a major research phase (add it to "what we've
  already researched")

After updating `context.md`, re-paste it into every agent's Project
instructions in Claude. It only takes a few minutes.

**Monthly habit — check the learning logs:**

Spend 10–15 minutes reading through the `learning-log.md` files.
Look for patterns: is the same agent flagging the same type of problem
repeatedly? That's a signal the system prompt needs updating, even if
no formal `proposed-update.md` has been created.

**When an agent consistently underperforms in one area:**

Edit its `system-prompt.md` directly. Add a new process step, tighten
the output format, or add an explicit constraint for the edge case
that keeps causing problems. Then update the Project instructions in
Claude to match.

---

## 9. Tips for better outputs

**Be specific about inputs.** The more precisely you describe the
design problem, the user's context, and what you need, the sharper
the output. Vague prompts produce general outputs.

**Give the agent the constraints upfront.** If you know there's a
platform constraint, a brand rule, or a stakeholder preference that
affects this task, mention it at the start. Don't wait to correct the
agent after it's produced the wrong thing.

**Paste content rather than describing it.** Where possible, paste
actual research transcripts, actual copy, actual spec text — rather
than summarising it. Agents work better with real material than
summaries of material.

**Let agents finish before redirecting.** Give an agent the space to
complete its full output before jumping in with corrections. A partial
output is harder to evaluate than a complete one.

**Use the orchestrator to figure out what you need.** If you're not
sure which agents to use, or in what order, just describe your
situation to the orchestrator. That's its job.

**Don't use agents for decisions that require taste.** Agents are
excellent at structure, evidence, and process. They're not equipped
to make judgment calls about what feels right for your brand, what
will resonate with your users, or what the right creative direction
is. That's yours.

**Treat all outputs as drafts.** Every agent output is raw material
for your thinking. Review it critically, edit it, challenge it. The
agents have no stake in being right — you do.

---

## 10. Troubleshooting

**The agent is ignoring part of my instructions.**

Check that your Project instructions contain all three files in order:
`system-prompt.md`, then `persona.md`, then `context.md`. If one is
missing or the paste was incomplete, the agent will behave
inconsistently.

**The agent is making design decisions instead of just reporting.**

This is a persona drift issue. Review the `persona.md` for that agent
and check the "Hard boundaries" section is still present in the Project
instructions. Sometimes long conversations can cause agents to drift —
starting a new conversation in the same Project usually fixes it.

**The agent keeps referencing a previous project.**

Claude Projects maintain conversation history within a Project, but
each new conversation starts fresh from the system prompt. If an agent
is referencing old work, it may be because the `_shared/context.md`
still contains outdated information. Update `context.md` and re-paste
it into the Project instructions.

**The agent's output format is wrong or inconsistent.**

The output format is specified in `system-prompt.md`. Open that file,
find the "Output format" section, and check whether the format
described there matches what you need. Edit it if not, then update
the Project instructions.

**The agent is being too verbose / too brief.**

This is a persona issue. Add an explicit instruction to `persona.md`
under "Output personality" — e.g. "Responses should be no longer than
one A4 page" or "Always include full detail — do not summarise."

**I'm not sure if the context.md update is reflected in Claude.**

After editing `context.md`, you must manually re-paste it into each
relevant Claude Project's instructions. Edits to local files do not
automatically sync to Claude.

---

## 11. Quick-start cheatsheet

```
FIRST-TIME SETUP
────────────────
1. Fill in _shared/context.md with your product details
2. For each agent (11 total):
   a. Create a new Claude Project with the agent's name
   b. Paste: system-prompt.md → persona.md → context.md
      (one blank line between each)
   c. Save Project instructions
3. Done. Start with the Orchestrator.

DAILY USE
──────────────────────────────────────────────────────
Goal is multi-step or unclear?   → Open Orchestrator
Single contained task?           → Open that agent directly
Prompt structure: task + input + constraints

PIPELINES
──────────────────────────────────────────────────────
New feature from scratch:
  Competitive research + User research
    → Insight synthesis → Design brief → Variations

Designs ready for engineering:
  Design system audit + Accessibility audit
    → Handoff → Design QA

MAINTENANCE
──────────────────────────────────────────────────────
Context changed?       → Update context.md, re-paste into all Projects
Agent underperforming? → Edit system-prompt.md, update Project
Proposed update in folder? → Review, apply if valid, delete the file
Monthly: skim learning-log.md files for patterns

AGENT QUICK REFERENCE
──────────────────────────────────────────────────────
Orchestrator           → Coordinates everything, start here for big goals
Competitive research   → How do competitors solve this?
User research          → What are users actually experiencing?
Insight synthesis      → What does the research mean for design?
Design brief           → What exactly are we designing and why?
Variations             → Give me real options to react to
Design system audit    → Are my designs consistent?
Copy & microcopy       → Write/review all in-product text
Accessibility audit    → Does this meet WCAG AA?
Handoff                → Engineering-ready specifications
Design QA              → Does the built product match the designs?
```

---

*Last updated: June 2025*
*This guide covers Claude.ai Projects as the primary tool. The same
principles apply to other AI tools that support persistent system
prompts.*
