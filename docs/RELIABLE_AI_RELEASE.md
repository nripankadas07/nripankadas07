# Reliable AI release architecture

## Thesis

The ten August 2026 repositories form a reference pipeline for systems that can
act, fail, recover, and leave evidence:

```text
requirements → executable workload → contract tests → capability inventory
             → policy decision → deterministic replay → trace analysis
             → tamper-evident record → reviewable evidence
```

## Control plane

| System | Responsibility | Boundary |
|---|---|---|
| SpecSpan | Requirement, code, and test traceability | Structured annotations, not arbitrary-prose interpretation |
| ToolDrill | Tool schema and failure-behavior testing | Offline conformance reference, not universal MCP certification |
| Agent SBOM | Component and capability inventory | Evidence-based heuristics, not malware proof |
| Trustline MCP | Deny-overrides policy, approval, quota, redaction, audit | Reference JSON-RPC boundary, not production identity infrastructure |
| RunMirror | Record, redact, replay, and locate first divergence | Explicit adapters, not invisible interception of every framework |
| Memory Gauntlet | Correction, forgetting, deletion, isolation, privacy tests | Synthetic scenarios, not a claim of universal memory quality |

## Workload plane

| System | Decision surface | Safety signal |
|---|---|---|
| Grid Ops Arena | Dispatch, storage, renewables, outage recovery | Unserved energy, illegal actions, recovery, cost, emissions |
| Carbon Risk Lab | Portfolio issuance and tail risk | Reversal, delay, default, policy, VaR/CVaR, sensitivities |
| Climate Evidence Bench | Quantitative climate/energy answers | Number, unit, year, geography, source, citation, time cutoff |
| Value Density Lab | Product outcomes and user cost | Completion quality, time, friction, cognitive load, regret, harm |

## Evidence compatibility

Each project owns a versioned native artifact because flattening every domain
into one schema would hide useful detail. Every deterministic demo also exposes:

- project and schema version;
- seed or fixed event order;
- input/configuration digest;
- summary metrics and status;
- generated artifact paths and digests;
- explicit limitations.

Those fields are designed for adapters into the existing TraceWeave,
SandboxLedger, and ProofDeck stack. Compatibility is claimed only when an
adapter and integration test exist.

## Release standard

- offline/no-key happy path;
- one command to test and one command to generate the demo;
- JSON plus a human-readable static report;
- malformed-input, boundary, determinism, and safety tests;
- CI, security notes, limitations, contribution workflow, and MIT license;
- `v0.1.0` release with honest alpha/reference status;
- no employer or private data;
- AI-assistance disclosure and no fabricated adoption claims.
