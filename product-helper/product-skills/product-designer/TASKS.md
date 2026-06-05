# Product Designer — Task List

A stage-by-stage guide for Product Design work from kick-off through to engineering handover.
Tasks marked **[MQB]** are Minimum Quality Bar — they must be complete before progressing.

---

## Phase 1 — Kick-off

Tasks to complete before design work begins.

### Understand the problem and user
- [ ] Read and confirm understanding of the problem statement from PM
- [ ] Confirm you agree with the problem statement — flag if it feels solution-shaped or unclear
- [ ] Name the primary user: who are they, what is their context, what are they trying to accomplish
- [ ] List the user needs that this design must address, ranked by priority
- [ ] Confirm what success looks like — what outcome should this design achieve after launch

### Establish scope and fidelity
- [ ] Confirm what is in scope for this design phase — get explicit clarity from PM
- [ ] Confirm what is explicitly out of scope — do not assume
- [ ] Agree on the fidelity expected at each stage and why (lo-fi for exploration, hi-fi for handoff, etc.)
- [ ] Clarify what the design output will be used for: exploration, user testing, stakeholder review, or engineering handoff

### Understand constraints
- [ ] Document technical and platform constraints that must be respected
- [ ] Review any existing design system, component library, or pattern guidelines
- [ ] List components and patterns available for use in this work
- [ ] Document accessibility requirements (WCAG level, known user needs)
- [ ] Note any brand, internationalisation, or responsive context requirements

### Establish process
- [ ] Agree how design will be validated — is user testing planned, and at what fidelity?
- [ ] Identify reviewers and agree review points with their purpose (exploration feedback vs sign-off)
- [ ] Define what done looks like for this phase before handover

**Kick-off gate**: Do not start designing until the problem statement, user needs, success criteria, and constraints are confirmed.

---

## Phase 2 — Exploration (Lo-fi)

Tasks for exploring ideas before committing to a direction.

### Ground the work before sketching
- [ ] Re-read the problem statement before starting any design work
- [ ] List the user needs this exploration must respond to
- [ ] Review relevant research findings and key user quotes
- [ ] Look at analogous solutions in adjacent products or industries — note what works and why

### Explore multiple directions
- [ ] Sketch or wireframe at least 3 different structural or conceptual approaches
- [ ] Do not polish any one idea before exploring alternatives
- [ ] For each approach, note the user need it addresses most strongly
- [ ] Identify which assumptions each approach depends on

### Review and narrow
- [ ] Share lo-fi explorations with PM — confirm alignment with problem and needs
- [ ] Identify which approach best addresses the primary user need
- [ ] Document why the other approaches were not taken forward
- [ ] Get internal feedback before committing to a direction

**Lo-fi gate**: At least 2 approaches explored and reviewed before progressing to structure.

---

## Phase 3 — Structure & Flow (Mid-fi)

Tasks for building out the validated concept into a complete, navigable structure.

### Build the primary flow
- [ ] Map the end-to-end user journey for the primary task
- [ ] Define clear entry points — how does the user arrive here?
- [ ] Define clear exit points — where does the user go when the task is complete?
- [ ] Resolve all decision branches — every yes/no/conditional path must lead somewhere

### Complete all flow states
- [ ] **[MQB]** Happy path — the primary successful user journey ✓
- [ ] **[MQB]** Error states — what happens when something fails or the user does something wrong ✓
- [ ] **[MQB]** Empty states — what the user sees when there is no content or data yet ✓
- [ ] Loading / skeleton states — transitions for async operations
- [ ] Edge cases — valid but non-standard paths (first-time user, returning user, partial data, etc.)
- [ ] Permission and access states — if the user doesn't have access or needs to upgrade
- [ ] Confirmation and success states — feedback when an action completes

### Apply structure principles
- [ ] Establish information hierarchy — what is most important on each screen?
- [ ] Keep interaction patterns consistent across screens
- [ ] Annotate key interactions and behaviours — not just how it looks, but how it works
- [ ] Check that layout and navigation patterns are consistent throughout the flow

### Design system alignment
- [ ] Identify which existing components are being used in this flow
- [ ] Note any places where no existing component fits — flag as a potential new pattern
- [ ] Do not create new components without first checking the system
- [ ] Use design tokens or variables — do not hardcode colour, spacing, or type values

### Validate at mid-fi
- [ ] Share mid-fi with PM — confirm all user needs are addressed and scope is correct
- [ ] Run a lightweight walkthrough with at least one stakeholder
- [ ] If user testing is planned: conduct tests at this fidelity before proceeding to hi-fi
- [ ] Incorporate feedback before increasing fidelity

**Mid-fi gate**: All flow states complete and mid-fi reviewed by PM before progressing to hi-fi.

---

## Phase 4 — Visual Design (Hi-fi)

Tasks for applying visual design and preparing for review or testing.

### Apply visual design
- [ ] Apply design system typography, colour, and spacing tokens
- [ ] Confirm colour contrast meets WCAG AA for all text and interactive elements
- [ ] Apply component variants correctly — use the right state for each context
- [ ] Ensure visual hierarchy is clear — the most important element is visually dominant

### Complete all visual states
- [ ] Default state
- [ ] Hover state (desktop)
- [ ] Active / pressed state
- [ ] Focus state (keyboard navigation visible)
- [ ] Disabled state
- [ ] Error state (inline validation, form errors, etc.)
- [ ] Empty state (no data, first use)
- [ ] Loading / skeleton state
- [ ] Success / confirmation state

### Responsive and adaptive design
- [ ] Design for all required breakpoints (mobile, tablet, desktop as applicable)
- [ ] Specify how layout, navigation, and content adapt at each breakpoint
- [ ] Address overflow, text truncation, and wrapping edge cases
- [ ] Test layouts at extremes — very long text, very short text, many items, few items

### Accessibility
- [ ] Colour contrast: text and UI components meet WCAG AA (4.5:1 for text, 3:1 for UI)
- [ ] Focus indicators are visible and consistent
- [ ] Keyboard navigation order is logical
- [ ] Interactive elements have clear labels (not icon-only without accessible labels)
- [ ] Complex interactions have screen reader / ARIA annotations where needed
- [ ] Content is not communicated by colour alone

### Validate at hi-fi
- [ ] Conduct user testing at hi-fi if not completed at mid-fi
- [ ] Share with PM and confirm design meets success criteria
- [ ] Conduct design critique or peer review
- [ ] Document findings from testing and incorporate key changes

**Hi-fi gate**: All visual states complete, WCAG AA contrast checked, and design validated before progressing to spec.

---

## Phase 5 — Specification & Handover to Engineering

Tasks for preparing a complete engineering-ready spec.

### Complete the specification
- [ ] **[MQB]** All screen states present and visually specified ✓
- [ ] **[MQB]** All user flows documented — happy, error, empty, and key edge cases ✓
- [ ] **[MQB]** All interactions and behaviours annotated (how it works, not just how it looks) ✓
- [ ] **[MQB]** Component spec: all components named and mapped to design system ✓
- [ ] **[MQB]** Accessibility requirements documented ✓
- [ ] Responsive behaviour specified for all breakpoints ✓
- [ ] Design tokens/variables used throughout — no hardcoded values ✓
- [ ] Assets exported and named to convention ✓
- [ ] Any new components documented and added to the design system ✓
- [ ] Open questions documented and triaged by priority ✓
- [ ] Key design decisions recorded with rationale ✓

### Pre-handover checklist
- [ ] Walk through the spec yourself end-to-end — does it cover every scenario?
- [ ] Check for any screen a user could reach that is not designed
- [ ] Check for any error a user could encounter that is not handled
- [ ] Confirm all components are from the design system or explicitly documented as new
- [ ] Confirm all token values are correct and consistent

### Handover to engineering
- [ ] Walk engineers through the design — do not just send files and a link
- [ ] Explain the key interactions and behaviours verbally
- [ ] Highlight any technically complex or non-standard interactions
- [ ] Confirm engineers understand the intent behind non-obvious decisions
- [ ] Point engineers to the open questions log
- [ ] Identify a design point of contact for questions during build

---

## Phase 6 — Stakeholder Sign-off (if required)

Tasks for presenting design for stakeholder approval.

### Prepare the presentation
- [ ] Open with the problem statement — establish what problem this design solves
- [ ] Show user needs being addressed — connect design decisions to user goals
- [ ] Explain key design decisions with rationale — do not just show visuals
- [ ] Make explicit what is in scope and what is not
- [ ] Disclose known gaps or open questions proactively
- [ ] State clearly what you are asking stakeholders to decide or approve
- [ ] End with next steps: what happens after sign-off, with owners and timelines

### During the review
- [ ] Listen for concerns — do not dismiss or immediately defend design decisions
- [ ] Distinguish preference feedback from problem feedback
- [ ] Note all feedback regardless of whether it is acted on
- [ ] Confirm what decisions were made in the session

### After the review
- [ ] Document feedback received and decisions made
- [ ] Communicate which feedback will be acted on and which will not, with reasons
- [ ] Update the design based on agreed changes before progressing

---

## Ongoing — Quality Self-Checks

Use these questions at any point during design work to check quality:

- Can I trace every significant design decision to a user need or research finding?
- Am I designing for the stated problem, or has it shifted — and does PM know?
- Have I explored more than one approach before committing to this direction?
- Beyond the happy path: have I considered error, empty, loading, and edge case states?
- Are all decision branches in the flow resolved?
- Is the fidelity appropriate for what this work is being used for right now?
- Am I using existing components and patterns, or introducing new ones unnecessarily?
- Are design decisions consistent across all screens in this flow?
- What assumptions are baked into this design that have not been tested?
- Is user testing planned — and are the right users being tested at the right fidelity?
- Is there anything in this design I am not comfortable with or uncertain about?
- Would I be confident walking an engineer through every screen and state right now?
