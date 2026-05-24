# Nripanka Das

**The No-Dependency AI + Systems Lab.** Small, readable, tested AI and
systems tools for developers who want code they can understand, run, audit, and
extend.

I am building a focused portfolio of compact Python and TypeScript libraries:
parsers, codecs, data structures, CLI tools, developer utilities, and a few AI
experiments. The bias is toward source you can read in one sitting, tests you
can run locally, and APIs that do one job without pulling in a dependency tree.

## Current Surface

- **100 public repositories inspected** on 2026-05-24.
- **99 project repositories** plus this profile repository.
- **98 runnable project repos passed local install + lint/type/test/build
  checks** in the audit environment.
- **2 docs-only repos**: this profile and `mlproject`, a public scratchpad that
  should stay public only if it is meant to be a transparent lab notebook.
- **No PyPI/npm publication is claimed here.** Install instructions are written
  for source checkouts until a package is intentionally published.

## Flagship Projects

| Project | Why It Matters |
|---|---|
| [`safejson`](https://github.com/nripankadas07/safejson) | Hardened JSON parsing with depth/size limits, duplicate-key detection, NaN/Infinity rejection, and type policy controls. |
| [`tomlmini`](https://github.com/nripankadas07/tomlmini) | Zero-dependency TOML common-subset parser with explicit edge-case behavior instead of silent guessing. |
| [`bencode`](https://github.com/nripankadas07/bencode) | Strict BitTorrent-style bencode encoder/decoder that rejects non-canonical encodings. |
| [`jsonptr`](https://github.com/nripankadas07/jsonptr) | RFC 6901 JSON Pointer parse/format/resolve/mutate library with typed errors. |
| [`globmatch`](https://github.com/nripankadas07/globmatch) | Glob matcher with extglob, POSIX classes, globstar support, and an AST-backed interpreter. |
| [`decimal-ts`](https://github.com/nripankadas07/decimal-ts) | BigInt-backed fixed-point decimal arithmetic for exact money-style calculations. |
| [`agent-framework`](https://github.com/nripankadas07/agent-framework) | Lightweight agent orchestration with tools, memory, and ReAct-style loops. |
| [`dep-audit`](https://github.com/nripankadas07/dep-audit) | Python dependency vulnerability scanner built around OSV.dev. |

## Library Index

### Parsers, Codecs, and Formats

[`tomlmini`](https://github.com/nripankadas07/tomlmini),
[`bencode`](https://github.com/nripankadas07/bencode),
[`safejson`](https://github.com/nripankadas07/safejson),
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

### Data Structures, Algorithms, and Math

[`decimal-ts`](https://github.com/nripankadas07/decimal-ts),
[`bitvec`](https://github.com/nripankadas07/bitvec),
[`trie`](https://github.com/nripankadas07/trie),
[`trie-ts`](https://github.com/nripankadas07/trie-ts),
[`path-trie`](https://github.com/nripankadas07/path-trie),
[`ringbuf`](https://github.com/nripankadas07/ringbuf),
[`rangeset`](https://github.com/nripankadas07/rangeset),
[`randpick`](https://github.com/nripankadas07/randpick),
[`numbertheory`](https://github.com/nripankadas07/numbertheory),
[`chunkby`](https://github.com/nripankadas07/chunkby),
[`flatdict`](https://github.com/nripankadas07/flatdict),
[`dotpath`](https://github.com/nripankadas07/dotpath),
[`levendist`](https://github.com/nripankadas07/levendist).

### Text, URLs, Shells, and Identifiers

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

### Time, Numbers, Units, and Color

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

### AI, DevEx, Security, and Product Tools

[`agent-framework`](https://github.com/nripankadas07/agent-framework),
[`ai-toolkit`](https://github.com/nripankadas07/ai-toolkit),
[`prompt-eval`](https://github.com/nripankadas07/prompt-eval),
[`rag-pipeline`](https://github.com/nripankadas07/rag-pipeline),
[`token-counter`](https://github.com/nripankadas07/token-counter),
[`schema-gen`](https://github.com/nripankadas07/schema-gen),
[`dep-audit`](https://github.com/nripankadas07/dep-audit),
[`env-vault`](https://github.com/nripankadas07/env-vault),
[`envdiff`](https://github.com/nripankadas07/envdiff),
[`diffstat`](https://github.com/nripankadas07/diffstat),
[`markdownlint`](https://github.com/nripankadas07/markdownlint),
[`log-parser`](https://github.com/nripankadas07/log-parser),
[`api-mocker`](https://github.com/nripankadas07/api-mocker),
[`config-loader`](https://github.com/nripankadas07/config-loader),
[`feature-flags`](https://github.com/nripankadas07/feature-flags),
[`rate-limiter`](https://github.com/nripankadas07/rate-limiter),
[`retryback`](https://github.com/nripankadas07/retryback),
[`retry-lib`](https://github.com/nripankadas07/retry-lib),
[`task-queue`](https://github.com/nripankadas07/task-queue),
[`startup-dashboard`](https://github.com/nripankadas07/startup-dashboard),
[`csv-explorer`](https://github.com/nripankadas07/csv-explorer),
[`cli-timer`](https://github.com/nripankadas07/cli-timer),
[`json-differ`](https://github.com/nripankadas07/json-differ),
[`mlproject`](https://github.com/nripankadas07/mlproject).

## Engineering Bar

Every serious project here should be easy to audit:

- A README that says what the library does and what it deliberately does not do.
- MIT license, security policy, contributing guide, and quality notes.
- Local test/build instructions that do not imply PyPI/npm availability.
- Zero runtime dependencies by default unless the domain genuinely needs them.
- CI and local checks for the package surface that exists today.

The best place to start is `safejson` for hostile input, `tomlmini` for format
edge cases, `decimal-ts` for exact arithmetic, or `globmatch` for parser-heavy
systems code.
