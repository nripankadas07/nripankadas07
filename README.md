# Nripanka Das

**The No-Dependency AI + Systems Lab:** practical AI, evaluation, parser,
security, and developer-tooling projects built to be read, run, tested, and
audited from a fresh checkout.

I build small systems that make complex AI and infrastructure ideas inspectable:
coding-agent evaluation, local-first RAG, prompt regression tests, safe parsing,
typed TypeScript primitives, and zero-dependency Python utilities. The profile is
curated around a few flagship projects first, then a smaller set of release-track
libraries.

The newest benchmark set is an **Internet Ownership Kit**: 10 compact,
self-hosted/local-first reference projects inspired by the kind of GitHub repos
that replace everyday big-tech services.

## Start Here

| Project | Why It Matters | First Demo |
|---|---|---|
| [PatchGym](https://github.com/nripankadas07/patchgym) | Mine real Git history into local SWE-bench-style coding-agent tasks with hidden tests and auditable oracle patches. | `bash scripts/demo.sh` |
| [agent-framework](https://github.com/nripankadas07/agent-framework) | A tiny visible agent runtime: plan, act, observe, remember, finish, with readable traces. | `python examples/no_api_key_agent.py` |
| [rag-pipeline](https://github.com/nripankadas07/rag-pipeline) | RAG from first principles: chunking, retrieval, citations, evaluation, and reports without hosted services. | `python examples/local_rag_demo.py` |
| [prompt-eval](https://github.com/nripankadas07/prompt-eval) | Prompt regression tests that can run in CI without secrets or hidden service calls. | `python examples/no_api_key_regression.py` |
| [safejson](https://github.com/nripankadas07/safejson) | JSON parsing treated as a security boundary with duplicate-key rejection, typed errors, and resource limits. | `python examples/security_boundary.py` |
| [decimal-ts](https://github.com/nripankadas07/decimal-ts) | Exact fixed-point decimal arithmetic for TypeScript, backed by `BigInt` instead of floating point. | `npm install && npm run demo` |

PatchGym is the best first run:

```bash
git clone https://github.com/nripankadas07/patchgym
cd patchgym
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
bash scripts/demo.sh
```

## Release Track

These are the projects I intend to keep release-ready, tested, and documented.
They represent the profile's strongest public surface.

| Area | Projects |
|---|---|
| AI and evaluation | [PatchGym](https://github.com/nripankadas07/patchgym), [agent-framework](https://github.com/nripankadas07/agent-framework), [rag-pipeline](https://github.com/nripankadas07/rag-pipeline), [prompt-eval](https://github.com/nripankadas07/prompt-eval), [token-counter](https://github.com/nripankadas07/token-counter) |
| Security and operations | [safejson](https://github.com/nripankadas07/safejson), [dep-audit](https://github.com/nripankadas07/dep-audit) |
| Parsers and data formats | [tomlmini](https://github.com/nripankadas07/tomlmini), [bencode](https://github.com/nripankadas07/bencode), [csvinfer](https://github.com/nripankadas07/csvinfer), [urlnorm](https://github.com/nripankadas07/urlnorm) |
| TypeScript primitives | [decimal-ts](https://github.com/nripankadas07/decimal-ts), [argv-zod](https://github.com/nripankadas07/argv-zod), [argv-strict](https://github.com/nripankadas07/argv-strict) |
| Terminal and text tooling | [wordwrap](https://github.com/nripankadas07/wordwrap) |

The release-track repositories have GitHub releases with build artifacts
attached: Python wheels/source distributions for Python projects and npm
tarballs for TypeScript projects.

Everything else is either a focused utility, a lab note, or an archive candidate.
The goal is depth, not repo-count theater.

## Internet Ownership Kit

Ten small projects for owning more of the internet workflows people usually rent
from platforms.

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

Each project has a README, CLI, tests, CI, quality docs, and a `v0.1.0` GitHub
release with wheel/source artifacts.

## Technical Essays

- [PatchGym: Local Coding-Agent Benchmarks From Real Git History](essays/patchgym-local-benchmarks.md)
- [Visible Agent Evaluation: Testing The Loop, Not The Demo](essays/visible-agent-evaluation.md)
- [Safe Local-First AI Tooling: Small Systems With Hard Boundaries](essays/local-first-ai-safety.md)

The six flagship repositories also include deeper architecture notes, release
notes, limitations, and runnable examples.

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
checks where possible, explicit limits, typed failure modes, and repeatable local
tests. For TypeScript packages, correctness means strict typechecking, tests,
build output, and package metadata that matches what is actually shipped.

## Current Focus

1. Keep the six flagships pinned and release-ready.
2. Maintain the release-track libraries with stronger examples, conformance tests, and
   publication-ready packaging.
3. Consolidate or archive scratchpads and unclear experiments instead of letting
   them dilute the profile.
4. Prefer runnable demos, release artifacts, and technical writing over vanity
   metrics.

## Contact

Open an issue on the relevant repository for bugs, design questions, or focused
collaboration. For profile-level context, use
[nripankadas07/nripankadas07](https://github.com/nripankadas07/nripankadas07).
