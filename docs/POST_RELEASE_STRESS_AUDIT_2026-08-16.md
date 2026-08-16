# Post-release stress and security audit — August 16, 2026

## Decision

The ten-project reliable-AI program passed its bounded post-release gate.
No reproducible in-scope release blocker remained after remediation and
independent re-audit.

This is not a claim that the software can never contain another defect. It is a
traceable statement about the tested commits, packages, workflows, security
alerts, and live proof surfaces described below.

## Verified outcome

- Ten public version 0.1.1 adversarial-hardening releases.
- Ten annotated tags dereference exactly to the current main commits.
- 299 tests per supported runtime, or 598 source-suite executions across two
  runtimes.
- A further 422 test executions from complete extracted Python source
  distributions, for 1,020 source-plus-sdist test executions.
- Sixteen clean package archives and ten checksum manifests published as 26
  GitHub release assets.
- All 26 live assets downloaded and byte-compared with the approved local
  release set.
- All 16 downloaded archives independently checksum-verified, installed, and
  exercised through their real command-line entry point and golden demo.
- Extended CodeQL with remote-and-local threat modeling configured on all ten
  repositories.
- Zero open CodeQL, Dependabot, or secret-scanning alerts across the ten
  repositories at the final gate.
- Three live GitHub Pages proof surfaces for Trustline MCP, Grid Ops Arena, and
  Value Density Lab.

## Test depth by repository

Counts below are the final source-suite counts on each supported runtime.
Python suites ran on 3.9.6 and 3.12.13. TypeScript suites ran on Node
22.23.2 and 24.13.1.

| Repository | Language | Tests per runtime | Version 0.1.1 release |
|---|---|---:|---|
| [agent-sbom](https://github.com/nripankadas07/agent-sbom) | Python | 31 | [Release](https://github.com/nripankadas07/agent-sbom/releases/tag/v0.1.1) |
| [carbon-risk-lab](https://github.com/nripankadas07/carbon-risk-lab) | Python | 33 | [Release](https://github.com/nripankadas07/carbon-risk-lab/releases/tag/v0.1.1) |
| [climate-evidence-bench](https://github.com/nripankadas07/climate-evidence-bench) | Python | 45 | [Release](https://github.com/nripankadas07/climate-evidence-bench/releases/tag/v0.1.1) |
| [grid-ops-arena](https://github.com/nripankadas07/grid-ops-arena) | Python | 32 | [Release](https://github.com/nripankadas07/grid-ops-arena/releases/tag/v0.1.1) |
| [memory-gauntlet](https://github.com/nripankadas07/memory-gauntlet) | Python | 34 | [Release](https://github.com/nripankadas07/memory-gauntlet/releases/tag/v0.1.1) |
| [runmirror](https://github.com/nripankadas07/runmirror) | TypeScript | 16 | [Release](https://github.com/nripankadas07/runmirror/releases/tag/v0.1.1) |
| [specspan](https://github.com/nripankadas07/specspan) | Python | 36 | [Release](https://github.com/nripankadas07/specspan/releases/tag/v0.1.1) |
| [tooldrill](https://github.com/nripankadas07/tooldrill) | TypeScript | 27 | [Release](https://github.com/nripankadas07/tooldrill/releases/tag/v0.1.1) |
| [trustline-mcp](https://github.com/nripankadas07/trustline-mcp) | TypeScript | 20 | [Release](https://github.com/nripankadas07/trustline-mcp/releases/tag/v0.1.1) |
| [value-density-lab](https://github.com/nripankadas07/value-density-lab) | TypeScript | 25 | [Release](https://github.com/nripankadas07/value-density-lab/releases/tag/v0.1.1) |
| **Total** |  | **299** | **10/10 public** |

## What the audit exercised

### Input, schema, and numerical boundaries

- malformed and unknown fields, duplicate identifiers, inherited properties,
  sparse arrays, non-finite numbers, oversized integers, invalid dates, unit
  conversion extremes, and contradictory schemas;
- energy conservation, bounded state and score invariants, Monte Carlo tail
  ordering, percentile plateaus, full-haircut boundaries, zero-tolerance
  evidence scoring, and deterministic seeded outputs;
- memory correction, deletion, expiry, role isolation, top-k reachability, and
  resistance to vacuous or diluted governance assertions.

### Security and filesystem boundaries

- child and ancestor symlinks, FIFOs, non-regular files, path traversal,
  descriptor failures, output-target substitution, rollback after ambiguous
  rename failure, stale locks, and concurrent bundle writers;
- secret-shaped values in replay divergence reports, Markdown and terminal
  control injection, prototype reads, arbitrary file correlation, and malformed
  audit chains;
- deterministic, parsed safe-regex subsets in Trustline MCP and ToolDrill,
  replacing attacker-influenced dynamic regular-expression execution.

### Resource and algorithmic stress

The regression suites were supplemented with bounded load and differential
tests. Representative gates included:

- 618,332 applied-domain assertions on each Python runtime before the final
  package re-audit;
- 5,001-file Agent SBOM scans including a file larger than 24 MiB;
- 20,000-node SpecSpan chains and rings plus seeded graph-oracle comparisons;
- 20,000 Trustline decisions, 20,000 RunMirror record-and-replay events, and
  10,000-session Value Density analyses;
- ToolDrill schema budgets that convert a former 1,998-property out-of-memory
  case into a controlled rejection;
- 205,335 ToolDrill safe-pattern comparisons with 702 generated-witness checks;
- 97,110 Trustline safe-pattern comparisons after rejecting the remaining
  Unicode-boundary ambiguity.

These are engineering stress probes, not real-world product performance
benchmarks.

## CodeQL and security review

The first extended CodeQL pass surfaced 40 open alerts. Every alert was reviewed.

- Sixteen findings were removed through code changes: fixed command dispatch,
  bounded parsed pattern engines, linear-time requirement parsing,
  least-privilege test file modes, property-safety controls, and explicit
  resource budgets.
- Twenty-four findings were dismissed with precise repository comments after
  manual validation: eighteen intentional local-path flows in the independently
  adversarial-tested Value Density writer, three local read-only sdist input
  paths, and three validated test-only archive extraction paths.

Dismissed does not mean hidden. It means the analyzer could not prove a boundary
whose contract and adversarial tests were reviewed explicitly.

At the final live query, all ten repositories reported:

- CodeQL state configured, extended query suite, remote-and-local threat model;
- zero open code-scanning alerts;
- zero open Dependabot alerts;
- zero open secret-scanning alerts.

## Package and release integrity

Release assets were built from clean archived main trees so ignored build output
could not contaminate packages. The gate rejected an earlier pre-release Node
asset set when stale compiled conflict copies were discovered, rebuilt the
archives, and verified the replacements.

The final live GitHub audit found:

- 26 of 26 custom assets downloaded successfully;
- 16 of 16 package archives matched their downloaded SHA256SUMS files;
- 26 of 26 downloaded assets were byte-identical to the approved release set;
- 12 of 12 Python wheel and sdist installs passed on the live-download gate;
- four of four Node tarball installs passed on the live-download gate;
- every installed CLI produced a byte-exact checked-in golden demo;
- no missing, extra, modified, or corrupt asset.

## Live proof surfaces

All three sites were manually redeployed from their final main commits. The
latest deployment SHA equals the corresponding release-tag target, HTTPS is
enforced, and each live body is byte-identical to its checked-in artifact.

| Site | Current deployment | Live artifact SHA-256 | Thirty-request p95 |
|---|---|---|---:|
| [Trustline MCP](https://nripankadas07.github.io/trustline-mcp/) | [Successful run](https://github.com/nripankadas07/trustline-mcp/actions/runs/31937899821) | 48ca1ef64fba16e80822b0af234fa3c121d5487be7fb8e34f212cfef4e9c800c | 247.872 ms |
| [Grid Ops Arena](https://nripankadas07.github.io/grid-ops-arena/) | [Successful run](https://github.com/nripankadas07/grid-ops-arena/actions/runs/31937901302) | 9c0b9ce46713c133ff3ec910b1338a26ea2e6cecf8fdca6e228a9181c73e5e82 | 198.455 ms |
| [Value Density Lab](https://nripankadas07.github.io/value-density-lab/) | [Successful run](https://github.com/nripankadas07/value-density-lab/actions/runs/31937902858) | 647bd99d556dd79626e71bd7e23551992e6a411c3ce683ee4cb8d85380dff9f7 | 249.838 ms |

A bounded cache-busted check issued 90 concurrent requests, thirty per site:
90 of 90 completed, 90 of 90 returned HTTP 200, and 90 of 90 matched the
expected content hash. Aggregate latency was 55.858 ms at p50, 245.533 ms at
p95, and 249.912 ms maximum during that run.

These are static, deterministic proof reports. They are not hosted production
services and do not imply real-world adoption.

## Findings that materially changed the release

The audit did more than rerun happy-path tests. It drove fixes for:

- fail-open policy decisions, quota overlap, approval semantics, unsafe dynamic
  regexes, and audit-chain validation;
- replay mutation and secret leakage, invalid cassette events, and report
  integrity;
- schema-witness explosion, Unicode string semantics, prototype bypasses, and
  server exception isolation;
- symlink disclosure, FIFO blocking, incomplete artifact validation, and
  non-transactional output publication;
- impossible grid charging, non-finite derived energy values, carbon percentile
  and CVaR edge cases, climate unit-conversion overflow, and zero-tolerance
  scoring;
- vacuous memory scores, unrelated correction evidence, top-k privacy dilution,
  recursive graph failure, malformed changed-file inputs, and source
  distribution incompleteness.

## Honest residual boundaries

- The six Python projects require Python 3.9 or newer; the four TypeScript
  projects are gated on Node 22 and 24.
- Cooperative artifact locks cannot make non-cooperating writers safe. The Node
  filesystem API also lacks descriptor-relative directory operations, so a
  documented concurrent ancestor-replacement limitation remains.
- Grid Ops Arena is a synthetic single-bus simulator, not power-flow or control
  software.
- Carbon Risk Lab uses synthetic, uncalibrated scenarios; arbitrary
  floating-point runs should record their runtime.
- Climate Evidence Bench verifies structured answer and citation metadata, not
  source-content truth or entailment.
- The tools remain public alpha/reference implementations. They have no external
  adoption evidence yet.

The profile snapshot remained one follower, one total star, and zero forks.
Those numbers are reported rather than optimized or embellished.

## Release gate conclusion

The ten repositories are live, installable, checksum-published, dual-runtime
tested, independently re-audited, and security-scanned. No reproducible
in-scope release blocker remained at the final gate.

The next meaningful proof is outside use: clean-checkout demo completions,
specific bug reports, external contributors, upstream integrations, and
maintenance over time.
