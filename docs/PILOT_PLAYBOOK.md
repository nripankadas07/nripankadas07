# Early-user recruitment and evidence plan

Starting point: no existing audience. These are **unsent invitations** and a
manual 30-day pilot plan, not evidence of adoption. The objective is to discover
whether strangers with relevant needs can complete a useful task, describe a
specific problem, and choose to return. A portfolio rating remains a judgment;
meeting a numeric target does not guarantee 9/10.

## Where to find testers

Channel research checked on 2026-10-11. Recheck in-community rules before posting;
membership and posting access have not been verified.

| Order | Project and audience | Entry point | Posting boundary |
| --- | --- | --- | --- |
| 1 | Value Density Lab: product managers, UX researchers, analysts | [Mind the Product Slack](https://www.mindtheproduct.com/product-management-slack-community/) | Its house rules explicitly allow product feedback in `#feedback`. Request criticism there; avoid promotional posts elsewhere. Join through the published invitation flow. |
| 2 | Trustline MCP: MCP developers and agent permission reviewers | [MCP community Discord](https://discord.com/servers/1312302100125843476) | The community lists project showcases. This is a community server, not a claim of official protocol endorsement. Exact channel rules require an in-server check before posting. |
| 3 | Grid Ops Arena: energy modelling educators and Python users | [Openmod forum categories](https://forum.openmod.org/categories) | Modelling includes model announcements. Use one relevant topic; [guidelines](https://forum.openmod.org/guidelines) prohibit spam and cross-posting. Explain the educational limits. |

For optional in-person discovery, [ProductTank](https://www.mindtheproduct.com/producttank/)
lists free local meetups, including Dubai. Attend as a participant, discuss the
measurement question, and invite a short review only when someone expresses
interest. Check the event's current registration, time, and venue first.

## First 30 days

1. Days 1–3: join the product community, read recent feedback threads, and give
   thoughtful feedback where you can. Publish the Value Density invitation once
   in the permitted feedback channel after authorization. Record its permalink
   and date. Offer the browser task first, then the local task to interested people.
2. Days 4–10: reply to volunteers, ask what they expected before helping, and
   record setup failures as well as successes. Publish the Trustline and Grid Ops
   invitations in their permitted channels after checking access and rules.
   Do not bulk-message strangers or use unrelated projects' issue trackers.
3. Days 11–20: choose the most common or serious blocker per project. Make a
   reviewable fix, link its merged change to the feedback issue, and invite one
   retest only when the tester has opted in. Keep contradictory feedback visible.
4. Days 21–30: count documented completions, specific feedback, and actual
   returns. Ask interested testers to apply a question from their own work.
   Publish a small evidence summary with limitations. Obtain exact quote approval
   separately; never transform polite praise or willingness into usage claims.

If a relevant invitation receives no response after a week, improve its task or
try one other permitted venue. Do not repost repeatedly. Low response is a
recruiting result, not evidence that the tool is useful or useless.

## Provisional targets and measurement

The following targets are learning goals for the first 30 days after invitations
are published. They are not benchmark-based forecasts and should be revised
after the first two weeks of actual responses. Starting usage is **unmeasured**.

| Measure | Definition / evidence | Provisional target per project |
| --- | --- | --- |
| Completed local tasks | Distinct external human testers who report a completed local task, version, and a concrete result in an issue or consented record. Exclude the maintainer, bots, and automated validation. Record assisted and unassisted completion separately. | 3 |
| Actionable feedback | Distinct external testers supplying an identifiable blocker, expected-versus-observed result, scoring counterexample, or concrete missing explanation. Browser reviewers and blocked attempts qualify; they do not automatically qualify as completed local tasks. | 3 |
| Actual return | A previously completing tester reports another useful task or a fix retest on a later date, at least seven days after their first completion. An intention to return is not a return. Record own-workflow use separately from repeating a bundled fixture. | 1 |

For recruiting diagnostics, record volunteers who start a task and their route.
For first-use friction, record approximate minutes to the first useful result
including setup, when supplied. Report completed/started counts with the route;
if fewer than ten people start, show counts rather than a persuasive percentage.
Show how many timing values are missing and keep blocked attempts visible.

Count a tester once per project per measure. The same person testing all three
is three project participations, not three unique people across the portfolio.
Self-reported results are user reports, not independently instrumented telemetry.
There is no tracking SDK, private-data upload, or automatic feedback collection.

Guardrails: preserve adverse feedback; do not recruit by offering stars or mutual
endorsements; keep confidential inputs private; obtain quotation approval. A
useful synthetic test demonstrates usability. A meaningful self-chosen task
demonstrates stronger usefulness; production adoption requires further evidence.

## Evidence log

No tester results are recorded at launch. Fill this table only from actual,
consented evidence. Public issue links are preferred; keep private recruitment
notes and contact details outside the public repository.

| Project | Feedback issue | Route | First task date | Completed / blocked | Specific observation | Fix link | Later-use date / task | Quote approved |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

[Baseline check](PILOT_BASELINE_2026-10-11.json) on 2026-10-11: all public issue history was read for the three
repositories (PRs excluded). Trustline had four owner-authored issues; the other
two had none. No non-owner, non-bot issue was found. This says nothing about
unreported use. [Trustline issues](https://github.com/nripankadas07/trustline-mcp/issues) ·
[Grid Ops issues](https://github.com/nripankadas07/grid-ops-arena/issues) ·
[Value Density issues](https://github.com/nripankadas07/value-density-lab/issues).

## Ready-to-review invitation: Value Density Lab

**For Mind the Product `#feedback`; not yet sent.**

I built Value Density Lab, an open-source reference for asking whether a product
helps people complete an intended outcome at a reasonable cost in time, friction,
and harm. I'm looking for three product managers, UX researchers, or analysts to
challenge its usefulness, especially its scoring assumptions.

The five-minute task is to inspect a synthetic invoice-flow report and tell me
which assumption you would challenge before using it in a product decision. No
installation is needed. A local task is available if you want to try your own
workflow definition. The sample does not prove a real product improvement or a
causal effect.

[Start the short task](https://github.com/nripankadas07/value-density-lab/blob/main/docs/USER_PILOT.md).
What is the first thing that would prevent you from using this method? Feedback
can go in the linked public GitHub form or this thread. Please keep private data
out of replies. I'm the maintainer, and candid criticism is welcome.

## Ready-to-review invitation: Trustline MCP

**For the MCP community's permitted showcase/feedback channel; not yet sent.**

I'm looking for three MCP developers or agent-tool reviewers to test Trustline
MCP, an open-source policy simulator with decision explanations and a verifiable
audit. The task is to explain an allow, deny, and approval decision, then optionally
change a quota locally and check whether the outcome matches your prediction.

[Browser review and local task](https://github.com/nripankadas07/trustline-mcp/blob/main/docs/USER_PILOT.md).
Where does the explanation fail to help you review a permission rule? A specific
confusing decision or sanitized counterexample would be useful.

I'm the maintainer. This is an experimental policy lab: it does not execute
upstream tools or authenticate approval identities, and its audit is unsigned.
Please use synthetic inputs. The linked GitHub feedback form is public; replying
in this thread is also fine.

## Ready-to-review invitation: Grid Ops Arena

**For one Openmod Modelling topic; not yet sent.**

Could three energy modelling educators, students, or Python developers help me
test whether Grid Ops Arena makes dispatch tradeoffs easier to explain? I built
this open-source, deterministic educational simulator to preserve requested and
feasible actions alongside reliability, cost, emissions, and constraint violations.

[Five-minute trace review and local experiment](https://github.com/nripankadas07/grid-ops-arena/blob/main/docs/USER_PILOT.md).
Try explaining one constraint violation, then optionally compare policies or lower
a synthetic battery power limit. Which trace detail or missing assumption would
make it unsuitable for a teaching exercise?

All bundled inputs are synthetic. It is an hourly single-bus teaching tool, not
a validated operational dispatch or planning model. I'm the maintainer and would
value concrete criticism. Reply here or use the linked public GitHub feedback
form; please do not share private grid data.

## Turn feedback into a case study

For each project, document the tester's task and relevant experience, the
observed problem, the resulting change, and a later-use result. Link the public
issue and merged fix. State the sample size and whether the task used bundled
synthetic input, a self-chosen synthetic example, or authorized real observations.
Publish an approved quote only in its original context. Add real outcome claims
to the profile only after the underlying evidence exists.
