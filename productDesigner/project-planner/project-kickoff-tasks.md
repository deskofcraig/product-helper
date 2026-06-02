# Project kick-off task list

A comprehensive checklist of tasks a product team should consider when
starting and running a project. Not every task applies to every project
— use the project planner agent to select, sequence, and adapt these
tasks based on your specific project type, stage, and constraints.

Tasks marked **(consider)** are situational — include them when they
apply, skip them when they don't.

---

## Phase 0 — Project initiation

These tasks happen before any phase begins. They align the team on
what the project is and how it will run.

### Alignment and setup
- [ ] Draft and agree on a problem statement
- [ ] Define the project goal (what does success look like?)
- [ ] Document why now (what signal or change makes this the right time?)
- [ ] Identify and confirm the team (designer, PM, engineering lead)
- [ ] Define the RACI (who is responsible, accountable, consulted,
      informed for each workstream)
- [ ] Identify key stakeholders and their interests
- [ ] Fill in the project kick-off template
- [ ] Schedule the Discovery Kick-off meeting
- [ ] **(consider)** Align on project type: new feature, redesign,
      iteration, or research only

### Inputs and signals
- [ ] Gather existing signals (support tickets, Planhat data, Amplitude,
      customer interviews already conducted)
- [ ] List existing documentation available (Dovetail, competitor
      analysis, prior research)
- [ ] Identify what is known vs. what needs to be discovered
- [ ] Consult the continuous discovery agent to frame the opportunity
      space and identify gaps

---

## Phase 1 — Research

Research runs before and alongside discovery. It builds the foundation
of knowledge the team needs to design well.

### Competitive and market research
- [ ] Identify 5–7 competitors or analogous products to review
- [ ] Run competitive research agent on the feature area or flow
- [ ] Document key patterns, differentiators, and design implications
- [ ] **(consider)** Identify in-market examples of like work to share
      with the team

### Existing user knowledge
- [ ] Review all available Dovetail research relevant to this problem
- [ ] Run user research agent on any existing transcripts, surveys,
      or session notes
- [ ] Identify gaps between what is known and what is needed
- [ ] **(consider)** Review Amplitude or analytics data for behavioural
      signals relevant to the problem space

### Synthesis
- [ ] Run insight synthesis agent on research outputs
- [ ] Document key insights, findings, and gaps in a Discovery Synthesis
      document
- [ ] Identify the primary opportunity and the assumptions underlying it
- [ ] Consult continuous discovery agent to validate opportunity framing
      and check for missed signals

---

## Phase 2 — Discovery

Discovery defines the problem space clearly enough to design with
confidence. It combines team alignment, assumption testing, and
user contact.

### Discovery kick-off
- [ ] Run Discovery Kick-off meeting
      - [ ] Present problem statement and goal
      - [ ] Share signals and existing research
      - [ ] Align on why now
      - [ ] Identify who the team can talk to (customers, internal
            subject matter experts)
      - [ ] **(consider)** Pre-shaping session: define the sandbox
            (scope, constraints, non-negotiables)
      - [ ] **(consider)** Co-ideation session with engineers to surface
            technical constraints early

### Planning artefacts
- [ ] Create project timeline
- [ ] Create Decisions document (a running log of decisions made and
      why)
- [ ] Create assumptions map (all assumptions the team is making,
      ranked by risk and certainty)
- [ ] Generate user stories
- [ ] Create workflow maps for the affected user journeys
- [ ] **(consider)** Generate scenarios from user stories

### Go-to-market planning
- [ ] **(consider)** Begin go-to-market plan (what support, docs, and
      comms will be needed at launch?)

### Assumption testing (5 sessions recommended)
- [ ] Identify the riskiest assumptions to test
- [ ] Consult continuous discovery agent to design the testing approach
- [ ] Recruit participants (see Participant Recruitment Playbook)
- [ ] Create agendas for all sessions at least 3 days prior
- [ ] **(consider)** Run an internal dry-run of the session agenda
- [ ] Run assumption testing session 1
- [ ] Run assumption testing session 2
- [ ] Run assumption testing session 3
- [ ] Run assumption testing session 4
- [ ] Run assumption testing session 5
- [ ] Synthesise findings from all assumption testing sessions
- [ ] Update assumptions map with what was learned

### Discovery synthesis and handover
- [ ] Complete Discovery Synthesis document (insights, findings, gaps)
- [ ] Run insight synthesis agent on all discovery outputs
- [ ] Organise alignment meeting before moving to wireframes
      (confirm problem space is correctly understood)
- [ ] Schedule and organise Discovery Hand-over meeting
- [ ] Run Discovery Hand-over meeting
      - [ ] Present synthesis findings to wider team
      - [ ] Confirm go / no-go to design phase
- [ ] Schedule Design Kick-off meeting

---

## Phase 3 — Design

Design transforms discovery insights into validated, ready-to-build
solutions.

### Design kick-off
- [ ] Run Design Kick-off meeting
      - [ ] Review discovery synthesis and brief
      - [ ] Align on design approach and constraints
      - [ ] Agree on what needs to be delivered
      - [ ] **(consider)** Align on Light & Dark mode requirements

### Brief and wireframing
- [ ] Run design brief agent to formalise the design brief
- [ ] Wireframe key flows and screens
- [ ] **(consider)** Share wireframes with engineering early for
      technical feasibility input
- [ ] Create requirements document for moving to high-fidelity:
      - [ ] List what is required to be delivered
      - [ ] List what is explicitly out of scope
- [ ] Organise alignment meeting before moving to high-fidelity designs
- [ ] Run alignment meeting — confirm wireframes correctly address
      the brief

### High-fidelity design
- [ ] Run variations agent to generate distinct design directions
- [ ] Run copy & microcopy agent for all in-product text
- [ ] Create high-fidelity designs
- [ ] Run design system audit agent on completed designs
- [ ] Run accessibility audit agent on completed designs
- [ ] **(consider)** Organise Initial Front-end Foundations critique
      with engineering
- [ ] **(consider)** Design team share and review (peer critique)
- [ ] Iterate on designs based on audit and critique feedback

### Prototype and usability testing
- [ ] Create interactive prototypes
- [ ] Create usability testing plan
      - [ ] Define what you are testing and why
      - [ ] Define success criteria for each test task
- [ ] Recruit participants (internal volunteers + external if possible)
- [ ] Create agendas for all sessions at least 3 days prior
- [ ] Run usability testing session 1
- [ ] Run usability testing session 2
- [ ] Run usability testing session 3
- [ ] Run usability testing session 4
- [ ] Run usability testing session 5
- [ ] Synthesise usability testing findings
- [ ] Run user research agent on usability session notes
- [ ] Iterate designs based on findings

### Design handover
- [ ] Run handoff agent to produce engineering-ready specifications
- [ ] Schedule and organise Design Hand-over meeting
- [ ] Run Design Hand-over meeting
      - [ ] Present designs and rationale (why now, why this direction)
      - [ ] Walk through new or modified components
      - [ ] Review handoff specifications with engineering
      - [ ] Flag open questions and engineering decisions needed
- [ ] **(consider)** Schedule Delivery Kick-off meeting

---

## Phase 4 — Delivery

Delivery takes the approved designs through to launch. The designer
remains involved to support engineering and ensure quality.

### Delivery kick-off
- [ ] Run Delivery Kick-off meeting
      - [ ] Confirm requirements and scope
      - [ ] Agree on build approach and sequencing
      - [ ] Set up QA checkpoints
- [ ] **(consider)** Final Front-end Foundations review before build
      begins

### Build support
- [ ] Create and refine engineering tickets
      - [ ] Each ticket references the relevant handoff spec
      - [ ] Edge cases and error states are explicitly ticketed
- [ ] Requirements documentation finalised and linked
- [ ] Be available for engineering questions during build
- [ ] **(consider)** Mid-build design check-in with engineering

### Quality assurance
- [ ] Run design QA agent: compare built UI against original designs
- [ ] Review QA findings with engineering
- [ ] Resolve Critical and Major discrepancies before launch
- [ ] **(consider)** Accessibility re-check on built product
- [ ] Sign-off on build fidelity

### Launch and roll-out
- [ ] Create roll-out plan:
      - [ ] Feature launch checklist completed
      - [ ] Support team briefed on new functionality
      - [ ] Documentation updates identified and scheduled
      - [ ] **(consider)** In-app announcement or onboarding for new
            feature
- [ ] Confirm go-live date with team
- [ ] Monitor post-launch signals (Amplitude, support tickets, Planhat)
      in first 2–4 weeks
- [ ] **(consider)** Schedule a post-launch retro or review session

---

## Standing checklist — applies to every project

These tasks are relevant at multiple points across all phases. Review
them at each phase transition.

- [ ] Decisions document is up to date
- [ ] Assumptions map reflects current understanding
- [ ] Context.md (shared agent file) is up to date with any new
      constraints or product changes
- [ ] Continuous discovery agent has been consulted if the opportunity
      framing has shifted
- [ ] Agent learning logs reviewed if a phase produced poor outputs
- [ ] Stakeholders are informed of progress at the end of each phase

---

*Task list version: 1.0*
*Based on: Octopus Deploy product team workflow + Continuous Discovery
Habits methodology*
*Maintained by: product design team*
