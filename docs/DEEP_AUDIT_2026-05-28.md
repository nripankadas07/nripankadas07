# Deep Portfolio Audit: May 28, 2026

This audit checked the live public GitHub profile after the five-project agent
evaluation launch: TraceWeave, RAGNeedle, Context Crucible, SandboxLedger, and
SpecMutate.

## External Bar

The strongest adjacent repositories are not winning because they have many
small utilities. They win because they make a hard technical identity obvious:

- LangChain presents itself as an agent engineering platform with quickstart,
  ecosystem, integrations, docs, releases, and community paths.
- LlamaIndex is positioned around document agents, OCR, RAG, attestations, and
  production-facing documentation.
- OpenAI Evals and DeepEval make evaluation a first-class workflow with
  registries, custom evals, metrics, and explicit setup.
- RagaAI Catalyst connects agent observability, tracing, debugging, monitoring,
  and evaluation into one operational story.

The profile strategy should therefore stay narrow: local-first infrastructure
for coding-agent benchmarks, RAG/eval stress tests, trace forensics, context
engineering, deterministic tests, and reproducible run ledgers.

## Live Operational Result

| Signal | Result |
|---|---|
| Public repositories | 116 |
| Active repositories | 115 |
| Archived repositories | 1 |
| Latest completed CI passing | 115/115 active repos |
| Deep-green operational score | 115/115 active repos |
| Repos with tests | 115/115 active repos |
| Repos with required hygiene docs | 115/115 active repos |
| Repos with docs/examples surface | 115/115 active repos |
| Open issue load | 0 |

Operational deep green means the repo is public and active, latest completed CI
is passing, tests are present, package metadata exists, required hygiene files
exist, and there is either a docs or examples surface.

## Actions Taken

- Added `docs/PROJECT_BRIEF.md` to 106 active repositories that had passing CI
  and tests but lacked a dedicated docs/examples surface.
- Added profile package metadata so the profile repo has an explicit tooling
  package surface for its link-check script.
- Re-ran the live portfolio audit after the changes.
- Confirmed no active repo is missing the operational audit gates.

## Strategic Finding

The portfolio is now operationally green, but not every repository should be
marketed as a mindblowing flagship. That is healthy. The public story should
make a clear distinction:

- **Flagship research stack:** PatchGym, TraceWeave, RAGNeedle, Context
  Crucible, SandboxLedger, SpecMutate.
- **Supporting AI/eval infrastructure:** agent-framework, rag-pipeline,
  prompt-eval, token-counter, ai-toolkit.
- **Correctness substrate:** safejson, tomlmini, bencode, urlnorm, csvinfer,
  jsonptr, jsonpatch-lite, iniparse, semverlite, digestlite.
- **TypeScript systems primitives:** decimal-ts, lru-ts, task-queue,
  tokenring-ts, eventbus-ts, decoder-ts, result-ts.
- **Local-first product labs:** lanbeam, rssdeck, passhouse, syncplan,
  readmine, photoflow, dnswarden, medialoom, chatmux, uptimelog.

## Next Technical Bar

To move from green to famous, the next work should deepen a small number of
repos rather than create more repos:

- PatchGym: sandboxed runner backend, replay manifests, failure taxonomy.
- TraceWeave: OpenTelemetry import, timeline SVG, benchmark aggregation.
- RAGNeedle: multi-hop needles, retriever adapter protocol, JSONL benchmark
  suite.
- Context Crucible: diff-aware scoring, symbol extraction, PatchGym adapter.
- SandboxLedger: signed records, OCI runtime metadata, replay verifier.
- SpecMutate: behavior-spec schema, parser adapters, PatchGym export.

This is the line: publish fewer new names, deepen the evaluation stack, and use
the utility repos as proof of correctness discipline.
