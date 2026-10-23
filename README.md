# Dr. Nripanka Das

I’m a product leader working on AI, energy and supply chain systems. I build
tools to test an idea, see where it fails, and make the results easy to check.

This is my independent project lab. The demos use synthetic data and show
software behavior, without claiming customer adoption or production results.

## Start here

### Trustline MCP

An agent can complete a task and still make a tool call it should have refused.
Trustline lets me test rules for allowing calls, denying them or asking for
review, then check the resulting audit trail.

The synthetic 11-entry fixture produces four allowed calls, five denials,
one approval requirement and one protocol error. Its audit chain verifies.
This is an experimental policy simulator with local MCP transports. It does
not execute upstream tools or authenticate approvals.

[Case study](docs/case-studies/trustline-mcp.md) ·
[Demo](https://nripankadas07.github.io/trustline-mcp/) ·
[Code](https://github.com/nripankadas07/trustline-mcp)

### Grid Ops Arena

A low-cost dispatch plan is not much use if it leaves demand unmet or asks
equipment to exceed its limits. Grid Ops Arena replays a microgrid policy and
shows the requested actions, feasible actions, cost, emissions and safety results.

In the synthetic 48-hour example, it serves 98.72% of demand, with 34.49 kWh
unserved and two constraint violations. Those failures stay visible in the
trace. This is an educational simulator.

[Case study](docs/case-studies/grid-ops-arena.md) ·
[Demo](https://nripankadas07.github.io/grid-ops-arena/) ·
[Code](https://github.com/nripankadas07/grid-ops-arena)

### Value Density Lab

More time in a product can mean that a task has become harder. This project
implements my Value Density framework to examine outcomes alongside time,
friction, regret and harm.

The demo compares two flows using 16 synthetic invoice sessions. It shows the
score components, completion rates and uncertainty. It illustrates a measurement
method; it does not establish a causal effect on real users.

[Case study](docs/case-studies/value-density-lab.md) ·
[Demo](https://nripankadas07.github.io/value-density-lab/) ·
[Code](https://github.com/nripankadas07/value-density-lab)

## Other projects

[PatchGym](https://github.com/nripankadas07/patchgym) turns Git history into
coding-agent tasks. [RunMirror](https://github.com/nripankadas07/runmirror)
records and replays agent behavior.
[Climate Evidence Bench](https://github.com/nripankadas07/climate-evidence-bench)
checks quantitative climate answers.

[Project index](docs/PROJECT_INDEX.md) ·
[Current health review](docs/HEALTH_REVIEW_2026-10-22.md) ·
[Release and validation history](docs/RELIABLE_AI_RELEASE.md)

## A little more about me

My work spans AI product leadership, energy and supply chain. These projects
are independent, with no employer branding or implied endorsement. I use AI
tools during development and disclose that use in each featured repository.

I want people to be able to take over when needed, inspect a decision and
understand what a benchmark can and cannot tell them.

If you try a project, [a short task and your feedback](docs/USER_PILOT.md)
would help. Bug reports, failed attempts and critical reviews are welcome in
the relevant repository.

[Find me on LinkedIn](https://www.linkedin.com/in/nripankadas/).
