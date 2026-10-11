# Reliable AI for high-stakes decisions

**Nripanka Das — AI product leader working across agent systems, energy,
climate, and product outcomes.**

I turn questions about safety, reliability, and user value into working tools
with decisions that can be replayed, inspected, and challenged.

## Three projects to start with

These independent projects show the problem, the design choices, and the proof.
Their demos use synthetic inputs; the results below demonstrate software
behavior, not customer adoption or production impact.

**Help shape the next release:** [try a short task and give feedback](docs/USER_PILOT.md).
Critical reviews and blocked attempts are welcome.

### Trustline MCP · Make agent tool decisions inspectable

**Problem:** a successful agent demo does not explain which tool calls should
be denied, require review, or leave an audit record.

**Built:** a policy simulator with deny-overrides rules, explicit approval
states, secret redaction, and a verifiable audit chain.

**Demonstrated:** an 11-entry attack fixture produces four allowed calls, five
denials, one approval requirement, and one protocol error; its audit verifies.
Experimental policy lab with local MCP transports; it does not execute upstream
tools or authenticate approvals.

[Read the case study](docs/case-studies/trustline-mcp.md) ·
[Open the demo](https://nripankadas07.github.io/trustline-mcp/) ·
[Explore the code](https://github.com/nripankadas07/trustline-mcp)

### Grid Ops Arena · Expose the tradeoffs in energy decisions

**Problem:** a dispatch policy can look efficient while leaving demand unmet
or requesting actions beyond equipment limits.

**Built:** a replayable microgrid simulator that records requested and feasible
actions, then reports reliability, cost, emissions, and safety together.

**Demonstrated:** the 48-hour synthetic scenario serves 98.72% of demand while
exposing 34.49 kWh of unserved energy and two constraint violations. The trace
makes those shortcomings visible. This is an educational simulator.

[Read the case study](docs/case-studies/grid-ops-arena.md) ·
[Open the demo](https://nripankadas07.github.io/grid-ops-arena/) ·
[Explore the code](https://github.com/nripankadas07/grid-ops-arena)

### Value Density Lab · Measure outcomes against user cost

**Problem:** time spent in a product can rise because a workflow is confusing.

**Built:** an executable reference for my Value Density framework, combining
outcome quality, time, friction, regret, and harm in an auditable report.

**Demonstrated:** 16 synthetic invoice sessions compare two flows while keeping
completion rates, scoring components, uncertainty, and guardrails visible.
The comparison illustrates the measurement method; it establishes no causal
effect on real users.

[Read the case study](docs/case-studies/value-density-lab.md) ·
[Open the demo](https://nripankadas07.github.io/value-density-lab/) ·
[Explore the code](https://github.com/nripankadas07/value-density-lab)

## More work

[PatchGym](https://github.com/nripankadas07/patchgym) turns Git history into
coding-agent tasks; [RunMirror](https://github.com/nripankadas07/runmirror)
records and replays agent behavior;
[Climate Evidence Bench](https://github.com/nripankadas07/climate-evidence-bench)
checks quantitative climate answers.

[Browse the project index](docs/PROJECT_INDEX.md) ·
[Current health review](docs/HEALTH_REVIEW_2026-10-11.md) ·
[Release and validation history](docs/RELIABLE_AI_RELEASE.md)

## About

I work across AI product leadership, energy, and supply chain. This is an
independent lab with no employer branding or implied endorsement. Development
uses AI assistance, disclosed in each featured repository.

My working principles: preserve human takeover, leave inspectable evidence,
expose the components of a score, and state the limits of a benchmark.

[Professional context and writing on LinkedIn](https://www.linkedin.com/in/nripankadas/).
For a reproducible bug or a useful integration, open an issue in the relevant
repository.
