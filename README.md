# Nripanka Das

**The No-Dependency AI + Systems Lab:** small, readable, tested AI and systems
tools for developers who want code they can run, understand, audit, and extend.

This profile is organized as a compact lab: a few flagship projects that carry
the main technical ideas, plus a catalog of small parser, systems, AI, DevEx,
and TypeScript libraries. The bias is toward source you can read in one sitting,
examples that run from a fresh clone, and documentation that explains the tradeoffs.

## Six Flagships To Pin

GitHub only gives the first impression room for a handful of repositories. These
six are the front door.

| Project | Technical Thesis | First Demo |
|---|---|---|
| [`PatchGym`](https://github.com/nripankadas07/patchgym) | Repo-specific coding-agent evaluation: mine real Git history into hidden-test tasks and grade whether agents actually fixed the code. | `bash scripts/demo.sh` |
| [`agent-framework`](https://github.com/nripankadas07/agent-framework) | Agents from scratch, but actually usable: a tiny inspectable runtime with tools, memory, traces, and safe no-key examples. | `python examples/no_api_key_agent.py` |
| [`rag-pipeline`](https://github.com/nripankadas07/rag-pipeline) | RAG from first principles: chunking, retrieval, citations, evaluation, and reports without hiding the retrieval loop. | `python examples/local_rag_demo.py` |
| [`prompt-eval`](https://github.com/nripankadas07/prompt-eval) | Unit tests for prompts: regression checks that can run in CI without API keys. | `python examples/no_api_key_regression.py` |
| [`safejson`](https://github.com/nripankadas07/safejson) | JSON parsing as a security boundary: duplicate-key detection, size/depth limits, and adversarial tests. | `python examples/security_boundary.py` |
| [`decimal-ts`](https://github.com/nripankadas07/decimal-ts) | Exact decimal arithmetic for money-style calculations in TypeScript, backed by `BigInt` instead of floats. | `npm install && npm run demo` |

### PatchGym

[PatchGym](https://github.com/nripankadas07/patchgym) turns any Git repository into a local SWE-bench-style coding-agent benchmark.

PatchGym mines real Git history, extracts hidden tests, verifies tasks, runs coding agents in local workspaces, and reports whether their patches actually pass.

```bash
git clone https://github.com/nripankadas07/patchgym
cd patchgym
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
bash scripts/demo.sh
```

Why it matters: public benchmarks are useful, but serious teams need to know whether agents can fix their own codebases.

Manual note: GitHub profile pins still need to be updated from the profile UI. PatchGym should be pinned first once the pin order is changed manually.

## Start Here

Each flagship is meant to be useful even if you only read it, and runnable in
less than five minutes from a clean checkout. PatchGym is the recommended first
run; the exact commands are in the card above.

```bash
git clone https://github.com/nripankadas07/decimal-ts
cd decimal-ts
npm install
npm run demo
npm test
```

The same pattern holds across the lab: clone, run the demo, run the tests, read
the limitations before using the library as a dependency.

## The Lab Catalog

### AI, Evaluation, And Local-First Tooling

[`PatchGym`](https://github.com/nripankadas07/patchgym),
[`agent-framework`](https://github.com/nripankadas07/agent-framework),
[`rag-pipeline`](https://github.com/nripankadas07/rag-pipeline),
[`prompt-eval`](https://github.com/nripankadas07/prompt-eval),
[`ai-toolkit`](https://github.com/nripankadas07/ai-toolkit),
[`token-counter`](https://github.com/nripankadas07/token-counter),
[`schema-gen`](https://github.com/nripankadas07/schema-gen).

### Security, Configuration, And Operational Tools

[`safejson`](https://github.com/nripankadas07/safejson),
[`dep-audit`](https://github.com/nripankadas07/dep-audit),
[`digestlite`](https://github.com/nripankadas07/digestlite),
[`env-vault`](https://github.com/nripankadas07/env-vault),
[`envdiff`](https://github.com/nripankadas07/envdiff),
[`config-loader`](https://github.com/nripankadas07/config-loader),
[`feature-flags`](https://github.com/nripankadas07/feature-flags),
[`rate-limiter`](https://github.com/nripankadas07/rate-limiter),
[`retryback`](https://github.com/nripankadas07/retryback),
[`retry-lib`](https://github.com/nripankadas07/retry-lib),
[`task-queue`](https://github.com/nripankadas07/task-queue),
[`api-mocker`](https://github.com/nripankadas07/api-mocker),
[`log-parser`](https://github.com/nripankadas07/log-parser).

### Parsers, Codecs, And Data Formats

[`tomlmini`](https://github.com/nripankadas07/tomlmini),
[`bencode`](https://github.com/nripankadas07/bencode),
[`jsonptr`](https://github.com/nripankadas07/jsonptr),
[`jsonpatch-lite`](https://github.com/nripankadas07/jsonpatch-lite),
[`iso8601`](https://github.com/nripankadas07/iso8601),
[`iniparse`](https://github.com/nripankadas07/iniparse),
[`urltemplate`](https://github.com/nripankadas07/urltemplate),
[`querystring`](https://github.com/nripankadas07/querystring),
[`dotenv-mini`](https://github.com/nripankadas07/dotenv-mini),
[`csvquote`](https://github.com/nripankadas07/csvquote),
[`csvinfer`](https://github.com/nripankadas07/csvinfer),
[`csvtable`](https://github.com/nripankadas07/csvtable),
[`csvtail`](https://github.com/nripankadas07/csvtail),
[`mdtable`](https://github.com/nripankadas07/mdtable),
[`mimedet`](https://github.com/nripankadas07/mimedet),
[`mimedb`](https://github.com/nripankadas07/mimedb),
[`hexdump`](https://github.com/nripankadas07/hexdump),
[`hexstr`](https://github.com/nripankadas07/hexstr),
[`morse`](https://github.com/nripankadas07/morse),
[`pigeon`](https://github.com/nripankadas07/pigeon).

### Matching, Text, URLs, And Shell Semantics

[`globmatch`](https://github.com/nripankadas07/globmatch),
[`wordwrap`](https://github.com/nripankadas07/wordwrap),
[`stringcase`](https://github.com/nripankadas07/stringcase),
[`slugify-x`](https://github.com/nripankadas07/slugify-x),
[`tinytemplate`](https://github.com/nripankadas07/tinytemplate),
[`tagged-template-ts`](https://github.com/nripankadas07/tagged-template-ts),
[`expand`](https://github.com/nripankadas07/expand),
[`pathmask`](https://github.com/nripankadas07/pathmask),
[`pathmatch-ts`](https://github.com/nripankadas07/pathmatch-ts),
[`shell-quote`](https://github.com/nripankadas07/shell-quote),
[`shellexpand`](https://github.com/nripankadas07/shellexpand),
[`urlnorm`](https://github.com/nripankadas07/urlnorm),
[`phonenumber-mini`](https://github.com/nripankadas07/phonenumber-mini),
[`uuidgen`](https://github.com/nripankadas07/uuidgen),
[`base62-ts`](https://github.com/nripankadas07/base62-ts).

### Data Structures, Algorithms, And Math

[`decimal-ts`](https://github.com/nripankadas07/decimal-ts),
[`bitvec`](https://github.com/nripankadas07/bitvec),
[`trie`](https://github.com/nripankadas07/trie),
[`trie-ts`](https://github.com/nripankadas07/trie-ts),
[`path-trie`](https://github.com/nripankadas07/path-trie),
[`ringbuf`](https://github.com/nripankadas07/ringbuf),
[`rangeset`](https://github.com/nripankadas07/rangeset),
[`tinycache`](https://github.com/nripankadas07/tinycache),
[`randpick`](https://github.com/nripankadas07/randpick),
[`numbertheory`](https://github.com/nripankadas07/numbertheory),
[`chunkby`](https://github.com/nripankadas07/chunkby),
[`flatdict`](https://github.com/nripankadas07/flatdict),
[`dotpath`](https://github.com/nripankadas07/dotpath),
[`levendist`](https://github.com/nripankadas07/levendist).

### Time, Numbers, Units, And Color

[`chronoparse`](https://github.com/nripankadas07/chronoparse),
[`crontab-lite`](https://github.com/nripankadas07/crontab-lite),
[`timeago`](https://github.com/nripankadas07/timeago),
[`durfmt`](https://github.com/nripankadas07/durfmt),
[`humanint`](https://github.com/nripankadas07/humanint),
[`numparse`](https://github.com/nripankadas07/numparse),
[`numfmt`](https://github.com/nripankadas07/numfmt),
[`unitcalc`](https://github.com/nripankadas07/unitcalc),
[`semverlite`](https://github.com/nripankadas07/semverlite),
[`cidrcalc`](https://github.com/nripankadas07/cidrcalc),
[`colortool`](https://github.com/nripankadas07/colortool),
[`colourdist`](https://github.com/nripankadas07/colourdist).

### TypeScript Building Blocks

[`result-ts`](https://github.com/nripankadas07/result-ts),
[`decoder-ts`](https://github.com/nripankadas07/decoder-ts),
[`argv-strict`](https://github.com/nripankadas07/argv-strict),
[`argv-zod`](https://github.com/nripankadas07/argv-zod),
[`parseopts-ts`](https://github.com/nripankadas07/parseopts-ts),
[`tsparser`](https://github.com/nripankadas07/tsparser),
[`tsmemo`](https://github.com/nripankadas07/tsmemo),
[`lru-ts`](https://github.com/nripankadas07/lru-ts),
[`eventbus-ts`](https://github.com/nripankadas07/eventbus-ts),
[`emitter-ts`](https://github.com/nripankadas07/emitter-ts),
[`tokenring-ts`](https://github.com/nripankadas07/tokenring-ts).

### Product, CLI, And Lab Notes

[`markdownlint`](https://github.com/nripankadas07/markdownlint),
[`diffstat`](https://github.com/nripankadas07/diffstat),
[`strtable`](https://github.com/nripankadas07/strtable),
[`startup-dashboard`](https://github.com/nripankadas07/startup-dashboard),
[`csv-explorer`](https://github.com/nripankadas07/csv-explorer),
[`cli-timer`](https://github.com/nripankadas07/cli-timer),
[`json-differ`](https://github.com/nripankadas07/json-differ),
[`mlproject`](https://github.com/nripankadas07/mlproject),
[`nripankadas07`](https://github.com/nripankadas07/nripankadas07).

## Quality Bar

Every active repository is expected to have:

- A specific README that says why the project exists and where it stops.
- MIT license, security policy, contribution guide, code of conduct, changelog,
  roadmap, and quality notes.
- Tests or an honest docs-only status.
- Source-checkout installation instructions until package publication is real.
- CI where a build or test surface exists.
- Issue templates and a pull request template.
- No fake package badges, fake benchmark numbers, or fake social proof.

For parsers and evaluators, correctness means adversarial inputs, conformance
checks where possible, explicit limits, and typed failure modes. For TypeScript
packages, correctness means typechecking, tests, build output, and package
metadata that matches what is actually shipped.

## Technical Essays

The flagship repositories include launch-ready technical notes:

- [`agent-framework/docs/TECHNICAL_ARTICLE.md`](https://github.com/nripankadas07/agent-framework/blob/main/docs/TECHNICAL_ARTICLE.md)
- [`patchgym/docs/TECHNICAL_ARTICLE.md`](https://github.com/nripankadas07/patchgym/blob/main/docs/TECHNICAL_ARTICLE.md)
- [`rag-pipeline/docs/TECHNICAL_ARTICLE.md`](https://github.com/nripankadas07/rag-pipeline/blob/main/docs/TECHNICAL_ARTICLE.md)
- [`prompt-eval/docs/TECHNICAL_ARTICLE.md`](https://github.com/nripankadas07/prompt-eval/blob/main/docs/TECHNICAL_ARTICLE.md)
- [`safejson/docs/TECHNICAL_ARTICLE.md`](https://github.com/nripankadas07/safejson/blob/main/docs/TECHNICAL_ARTICLE.md)
- [`decimal-ts/docs/TECHNICAL_ARTICLE.md`](https://github.com/nripankadas07/decimal-ts/blob/main/docs/TECHNICAL_ARTICLE.md)

## Roadmap

1. Keep the six flagships pinned and release-ready.
2. Promote 15-25 core libraries with stronger examples, conformance tests, and
   packaging metadata.
3. Consolidate redundant utilities instead of growing the repo count for its own
   sake.
4. Mark weak or unclear projects as `Needs Repair` or `Archive Candidate` before
   deciding whether to keep them public.

## Contact

Open an issue on the relevant repository for bugs, design questions, or focused
collaboration. For profile-level context, use
[`nripankadas07/nripankadas07`](https://github.com/nripankadas07/nripankadas07).
