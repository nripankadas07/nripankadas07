# Nripanka Das

**Agentic AI Infrastructure:** local coding-agent benchmarks, trace forensics,
RAG stress tests, context engineering, reproducibility ledgers, and safety
boundaries for tools that can be inspected from a fresh source checkout.

I build small infrastructure around agentic systems: benchmark generation, agent
runtimes, prompt regression testing, retrieval pipelines, hardened parsers, and
local-first developer tools. The pinned repositories are the main story; the
utility libraries are the disciplined substrate underneath them.

## Start Here

| Project | Why It Matters | First Demo |
|---|---|---|
| [PatchGym](https://github.com/nripankadas07/patchgym) | Mine real Git history into local SWE-bench-style coding-agent tasks with hidden tests and auditable oracle patches. | `bash scripts/demo.sh` |
| [TraceWeave](https://github.com/nripankadas07/traceweave) | Agent trajectory forensics: loop detection, causal edges, context drift, and risk reports from local JSONL traces. | `traceweave analyze examples/trace.jsonl` |
| [RAGNeedle](https://github.com/nripankadas07/ragneedle) | Adversarial RAG needle benchmark generation with deterministic retrieval metrics and distractor pressure. | `ragneedle demo --json` |
| [Context Crucible](https://github.com/nripankadas07/context-crucible) | Budgeted repository context packing for coding agents with salience scoring and leakage guards. | `context-crucible pack . --task "fix parser"` |
| [SandboxLedger](https://github.com/nripankadas07/sandboxledger) | Content-addressed run ledgers for reproducible agent and benchmark evaluations. | `sandboxledger verify ledger.jsonl` |
| [SpecMutate](https://github.com/nripankadas07/specmutate) | Metamorphic test-vector generation for parsers, CLIs, normalizers, and developer tools. | `specmutate demo --json` |

PatchGym is the flagship and the best first run:

```bash
git clone https://github.com/nripankadas07/patchgym
cd patchgym
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
bash scripts/demo.sh
```

## May 28, 2026 Research Launch

The newest five projects are designed as a coherent evaluation stack around
PatchGym:

- TraceWeave explains failed or wasteful agent trajectories.
- RAGNeedle stress-tests retrieval under adversarial evidence placement.
- Context Crucible decides what code context an agent should see.
- SandboxLedger records run integrity with hash chains and Merkle roots.
- SpecMutate generates deterministic metamorphic tests for the small tools
  agents often modify.

They are intentionally source-checkout runnable, dependency-light, and honest
about being research prototypes rather than adoption-inflated frameworks.

## How This Is Built

I use AI heavily for scaffolding, test generation, edge-case brainstorming, and
first-pass documentation. The design direction, architecture choices, project
boundaries, quality bar, and final review are mine.

My workflow is simple: AI-assisted output has to survive source-checkout setup,
local tests, CI, release packaging, security notes, limitations notes, and
manual review before it becomes part of the public portfolio. That is why the
profile emphasizes reproducible demos and auditable artifacts instead of vague
claims.

## Supporting Infrastructure

These release-track projects support the agentic AI infrastructure theme. They
are not competing with the flagships for attention; they are the pieces that
make agent workflows easier to test, parse, package, and reason about.

| Area | Projects |
|---|---|
| AI and evaluation | [PatchGym](https://github.com/nripankadas07/patchgym), [TraceWeave](https://github.com/nripankadas07/traceweave), [RAGNeedle](https://github.com/nripankadas07/ragneedle), [SandboxLedger](https://github.com/nripankadas07/sandboxledger), [SpecMutate](https://github.com/nripankadas07/specmutate), [agent-framework](https://github.com/nripankadas07/agent-framework), [rag-pipeline](https://github.com/nripankadas07/rag-pipeline), [prompt-eval](https://github.com/nripankadas07/prompt-eval), [token-counter](https://github.com/nripankadas07/token-counter) |
| Context engineering | [Context Crucible](https://github.com/nripankadas07/context-crucible), [PatchGym](https://github.com/nripankadas07/patchgym), [rag-pipeline](https://github.com/nripankadas07/rag-pipeline) |
| Security and operations | [safejson](https://github.com/nripankadas07/safejson), [dep-audit](https://github.com/nripankadas07/dep-audit) |
| Parsers and data formats | [tomlmini](https://github.com/nripankadas07/tomlmini), [bencode](https://github.com/nripankadas07/bencode), [csvinfer](https://github.com/nripankadas07/csvinfer), [urlnorm](https://github.com/nripankadas07/urlnorm) |
| TypeScript primitives | [decimal-ts](https://github.com/nripankadas07/decimal-ts), [argv-zod](https://github.com/nripankadas07/argv-zod), [argv-strict](https://github.com/nripankadas07/argv-strict) |
| Terminal and text tooling | [wordwrap](https://github.com/nripankadas07/wordwrap) |

The release-track repositories have GitHub releases with build artifacts:
Python wheels/source distributions for Python projects and npm tarballs for
TypeScript projects.

## Internet Ownership Kit

Ten compact projects for owning more of the internet workflows people usually
rent from platforms. They sit beside the AI work as local-first infrastructure
practice.

| Project | Inspired By | Job |
|---|---|---|
| [lanbeam](https://github.com/nripankadas07/lanbeam) | LocalSend | Local network file drops with one-time share tokens. |
| [rssdeck](https://github.com/nripankadas07/rssdeck) | FreeTube | No-account RSS and YouTube feed dashboard generator. |
| [passhouse](https://github.com/nripankadas07/passhouse) | Vaultwarden | Small encrypted local secrets vault with explicit safety notes. |
| [syncplan](https://github.com/nripankadas07/syncplan) | Syncthing | Directory snapshot and sync-plan engine before copying bytes. |
| [readmine](https://github.com/nripankadas07/readmine) | Ladder | Ethical offline reader for public pages you can access. |
| [photoflow](https://github.com/nripankadas07/photoflow) | Immich | Local photo inventory, duplicate detection, and album planning. |
| [dnswarden](https://github.com/nripankadas07/dnswarden) | AdGuard Home | Compile hosts-style blocklists into clean DNS sinkhole rules. |
| [medialoom](https://github.com/nripankadas07/medialoom) | Jellyfin | Static local media catalog for movies, shows, music, and audiobooks. |
| [chatmux](https://github.com/nripankadas07/chatmux) | LibreChat | Provider-neutral chat transcript hub with no-key local mocks. |
| [uptimelog](https://github.com/nripankadas07/uptimelog) | Uptime Kuma | Tiny uptime monitor with JSON logs and static status pages. |

Each project has a README, CLI, tests, CI, quality docs, contribution templates,
and a `v0.1.0` GitHub release with wheel/source artifacts.

## Technical Essays

- [PatchGym: Local Coding-Agent Benchmarks From Real Git History](essays/patchgym-local-benchmarks.md)
- [Visible Agent Evaluation: Testing The Loop, Not The Demo](essays/visible-agent-evaluation.md)
- [Safe Local-First AI Tooling: Small Systems With Hard Boundaries](essays/local-first-ai-safety.md)

The flagship repositories include architecture notes, release notes,
limitations, quality notes, and runnable examples.

## Live Audit Snapshot

Last audited on **May 28, 2026** across the public GitHub profile.

| Signal | Current State |
|---|---|
| Public repositories | 116 total: 115 active, 1 archived scratchpad |
| Active repo hygiene | 115/115 have README, license metadata, license file, CI, issue templates, and PR templates |
| CI state | 115/115 active repos have a latest completed GitHub Actions run passing |
| Research launch | 5 new local-first agent/eval projects shipped on May 28, 2026, all public and green |
| Release track | 25 repositories with `v0.1.0` GitHub releases and build artifacts |
| Internet Ownership Kit | 10/10 projects shipped with CLI, tests, CI, docs, releases, and contribution templates |
| Open issue load | 0 open issues across active repositories at audit time |

The detailed audit note is in
[docs/PORTFOLIO_AUDIT.md](docs/PORTFOLIO_AUDIT.md).
The latest deep audit is in
[docs/DEEP_AUDIT_2026-05-28.md](docs/DEEP_AUDIT_2026-05-28.md).

## Quality Bar

Every active repository is expected to have:

- a specific README that says why the project exists and where it stops;
- a license, security policy, contribution guide, code of conduct, changelog,
  roadmap, and quality notes;
- tests or an honest docs-only status;
- source-checkout installation instructions until registry publication is real;
- CI where a build or test surface exists;
- issue templates and a pull request template;
- no fake package badges, fake benchmark numbers, or fake social proof.

For parsers and evaluators, correctness means adversarial inputs, conformance
checks where possible, explicit limits, typed failure modes, and repeatable
local tests. For TypeScript packages, correctness means strict typechecking,
tests, build output, and package metadata that matches what is actually shipped.

## Professional Context

This GitHub profile is intentionally code-first. Career credentials, product
leadership context, and publication context live on
[LinkedIn](https://www.linkedin.com/in/nripankadas/).

Open an issue on the relevant repository for bugs, design questions, or focused
collaboration. For profile-level context, use
[nripankadas07/nripankadas07](https://github.com/nripankadas07/nripankadas07).

## What To Read First

- [PatchGym](https://github.com/nripankadas07/patchgym): the flagship, because
  it turns real Git history into coding-agent tasks with hidden tests and oracle
  patches.
- [TraceWeave](https://github.com/nripankadas07/traceweave): the quickest way
  to see the new failure-forensics direction.
- [Visible Agent Evaluation](essays/visible-agent-evaluation.md): the testing
  thesis behind the profile, focused on evaluating the loop instead of the demo.
