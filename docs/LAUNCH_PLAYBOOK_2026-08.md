# Launch and adoption playbook — August 2026

## Launch one program, not ten announcements

Lead with the falsifiable thesis:

> High-stakes agents should have the same things we expect from critical
> software: scoped authority, adversarial tests, deterministic replay, explicit
> human takeover, and evidence another engineer can inspect.

The three public proof stories are:

1. **Trustline MCP:** a malicious/off-policy tool request is denied, redacted,
   and written into a verifiable audit chain.
2. **Grid Ops Arena:** an unsafe policy violates a constraint while a safe
   policy recovers the same seeded outage with an inspectable score.
3. **Value Density Lab:** a five-minute high-friction workflow stops looking
   like “great engagement” when outcomes and user costs are measured together.

The other seven repositories are components and benchmarks inside that story.

## First 72 hours

- Publish one 60–90 second screen recording for each flagship. Show command,
  failure, report, and limitation; avoid a narrated feature tour.
- Share one technical LinkedIn post per flagship, separated by at least a day.
  Use the existing human-takeover narrative as the bridge to Trustline MCP and
  Grid Ops Arena.
- Share an X thread only after confirming the correct account. No X handle was
  verifiably linked during the audit.
- Invite specific technical review: one MCP policy edge case, one grid scoring
  counterexample, or one Value Density anti-gaming scenario.
- Open three good-first issues per flagship that produce a real adapter, fixture,
  or failing test—not cosmetic chores.

## First 30 days

### Week 1 — reproducibility

- Have three people outside the author run each flagship demo from a clean checkout.
- Convert every setup failure into a test or clearer error.
- Publish the exact test matrix and known environment gaps.

### Week 2 — interoperability

- Add one real MCP server fixture to ToolDrill and Trustline MCP.
- Add RunMirror or TraceWeave adapters to one external agent framework.
- Publish a PatchGym task corpus and baseline manifest.

### Week 3 — upstream credibility

- Contribute a focused fix, fixture, or documentation improvement to at least
  two upstream projects used in this work.
- Ask maintainers for technical feedback without asking for stars.
- Document accepted and rejected design feedback publicly.

### Week 4 — releases

- Cut `v0.2.0` only where user evidence justifies a change.
- Publish before/after benchmark methodology and raw artifacts.
- Consolidate or archive any new repository that has no independent job after
  integration experience.

## Metrics

Track completed demos, unique cloners where available, outside issues,
contributors, release downloads, upstream merges, benchmark replications, and
repeat visitors. Do not optimize for raw repository count, contribution-graph
density, or stars disconnected from use.

## Draft LinkedIn launch opener

> Last month I wrote that the most important part of an AI-controlled fighter
> jet was not the AI. It was the switch that gave the human immediate control.
>
> I turned that principle into code. Reliable AI for high-stakes decisions is a
> ten-part open-source lab for policy boundaries, tool testing, replay, memory
> governance, and evidence—proved against deterministic grid, carbon, climate,
> and product systems. The demos need no API key, and every score exposes its
> assumptions and failure modes.

Follow with one concrete GIF and one repository link. Put the full suite link in
a comment or final paragraph; do not ask for engagement before showing proof.
