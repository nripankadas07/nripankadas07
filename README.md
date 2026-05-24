# Hi, I'm Nripanka.

I'm building 120 small open-source libraries in 60 nights. Two a
night, every night. The kind of libraries you wish existed when you
just want one focused job done without dragging in a hundred
transitive dependencies.

So far: **99 of 120 done.**

## How I work

I write tests before code. Every project here lives or dies by its
test suite. Coverage gates are explicit, branch-aware where the
tooling supports it, and enforced in CI instead of left as a local
promise. If a branch can't be reached, I either test it, simplify it,
or delete it.

Python projects pass `mypy --strict`. TypeScript projects pass
`tsc --strict --noEmit` with the full strictness panel turned on
(`exactOptionalPropertyTypes`, `noImplicitAny`, the lot). Functions
stay under 30 lines. Nesting stays under 3 levels. I verify both
with an AST walk before every push.

Almost everything is zero runtime dependencies. When I need a
parser, I write the parser. When I need a date library, I write
the date library. The point of this sprint is to get good at the
fundamentals, not to glue other people's code together.

Every repo has an MIT license, a real README with install
instructions, a quick-start example, an API reference, and a
section explaining how to run the tests yourself.

## Current quality audit

On May 24, 2026, I started a deeper hardening pass across the public
portfolio. Each upgraded repo has to clear a stricter gate before I
mark it done: current GitHub Actions majors, blocking lint/type checks,
coverage enforcement, package build and smoke tests, security-alert
review, and remote GitHub CI verification.

Baseline portfolio sweep: **100 of 100 public repos checked**. The
current default branches have no recent failing GitHub Actions runs,
zero open Dependabot alerts, and zero open secret-scanning alerts. The
shared baseline now includes modern GitHub Actions majors, no soft-fail
lint/test steps, repo-level `SECURITY.md`, `CONTRIBUTING.md`, and
`QUALITY.md`, clean Python ruff checks, and TypeScript packages with a
standard `npm run typecheck` gate.

Upgraded projects so far:

- [`tomlmini`](https://github.com/nripankadas07/tomlmini): green on Python
  3.10, 3.11, and 3.12 with blocking ruff, `mypy --strict`, TOML conformance
  tests, a coverage floor, a clean package build, a green dependency graph run,
  and zero open Dependabot or secret-scanning alerts.
- [`bencode`](https://github.com/nripankadas07/bencode): green on Python 3.10,
  3.11, and 3.12 with blocking ruff, `mypy --strict`, BEP 3 canonical-format
  checks, 100% line and branch coverage, a clean package build, a green
  dependency graph run, and zero open Dependabot or secret-scanning alerts.
- [`safejson`](https://github.com/nripankadas07/safejson): green on Python 3.9,
  3.10, 3.11, and 3.12 with blocking ruff, `mypy --strict`, RFC 8259
  conformance checks, 100% line and branch coverage, wheel/sdist build and
  wheel smoke tests, a green dependency graph run, and zero open Dependabot or
  secret-scanning alerts.
- [`jsonptr`](https://github.com/nripankadas07/jsonptr): green on Python 3.9,
  3.10, 3.11, and 3.12 with blocking ruff, `mypy --strict`, RFC 6901 pointer
  and URI-fragment conformance checks, 100% line and branch coverage,
  wheel/sdist build and wheel smoke tests, a green dependency graph run, and
  zero open Dependabot or secret-scanning alerts.

## What's in here

### Parsers and codecs

These are the projects I'd reach for if I were stranded on a desert
island with a config file and one Python interpreter.

[`tomlmini`](https://github.com/nripankadas07/tomlmini) parses the
common subset of TOML 1.0. It handles tables, arrays of tables,
inline tables, datetimes, all four string flavours, and the full
numeric grammar with `_` separators. It deliberately rejects the
ambiguous dotted-key edge cases the full spec normalises away,
because I'd rather fail loudly than guess.

[`bencode`](https://github.com/nripankadas07/bencode) does
BitTorrent-style bencode encoding and decoding. Round-trips are
bit-exact. Non-canonical encodings get rejected: leading zeros,
`i-0e`, out-of-order or duplicated dict keys, trailing data — all
of it fails fast.

[`safejson`](https://github.com/nripankadas07/safejson) is what I
wish the standard library shipped. It's a hardened JSON parser
with configurable depth limits, string-length caps, duplicate-key
detection, NaN/Infinity rejection, and type whitelisting. There's
a streaming pre-scan that catches syntax errors, non-JSON numeric
constants, and resource-exhaustion attacks before `json.loads`
builds containers; duplicate-key and type policies run through
stdlib decode hooks immediately after that scan.

[`jsonptr`](https://github.com/nripankadas07/jsonptr) is a clean
RFC 6901 JSON Pointer implementation. Parse, format, escape,
format URI fragments, resolve, get, has, set, remove — all on
nested dicts and lists, with a tidy error tree that tells you
exactly where resolution failed.

[`iso8601`](https://github.com/nripankadas07/iso8601) is a strict
ISO-8601 parser covering dates, times, datetimes, durations, and
all four week-date and ordinal forms. Timezone offsets work,
fractional seconds work, and the round-trip formatters give you
back the canonical representation.

[`morse`](https://github.com/nripankadas07/morse) does
International Morse Code with prosigns and Farnsworth timing.
Yes, the Farnsworth ratio is correct (I checked the original
1959 paper).

Other parsers and codecs:
[`iniparse`](https://github.com/nripankadas07/iniparse),
[`querystring`](https://github.com/nripankadas07/querystring),
[`urltemplate`](https://github.com/nripankadas07/urltemplate),
[`csvquote`](https://github.com/nripankadas07/csvquote),
[`csvtable`](https://github.com/nripankadas07/csvtable),
[`csvtail`](https://github.com/nripankadas07/csvtail),
[`csvinfer`](https://github.com/nripankadas07/csvinfer),
[`mdtable`](https://github.com/nripankadas07/mdtable),
[`dotenv-mini`](https://github.com/nripankadas07/dotenv-mini),
[`hexdump`](https://github.com/nripankadas07/hexdump),
[`hexstr`](https://github.com/nripankadas07/hexstr),
[`urlnorm`](https://github.com/nripankadas07/urlnorm),
[`mimedet`](https://github.com/nripankadas07/mimedet),
[`mimedb`](https://github.com/nripankadas07/mimedb),
[`phonenumber-mini`](https://github.com/nripankadas07/phonenumber-mini).

### Numbers and time

[`decimal-ts`](https://github.com/nripankadas07/decimal-ts) is
arbitrary-precision fixed-point decimal arithmetic on `BigInt`,
with the seven rounding modes anyone doing money work actually
needs (the half-even mode is correct, not approximated). `0.1 +
0.2` returns `0.3`, the way it should have all along.

[`numbertheory`](https://github.com/nripankadas07/numbertheory)
is the bag of helpers I keep wanting in Project Euler problems:
extended Euclidean, Miller-Rabin primality, modular inverse,
factorisation, Euler phi, Möbius, CRT, Jacobi and Legendre
symbols. Pure Python, no SymPy.

[`humanint`](https://github.com/nripankadas07/humanint),
[`numparse`](https://github.com/nripankadas07/numparse),
[`numfmt`](https://github.com/nripankadas07/numfmt),
[`durfmt`](https://github.com/nripankadas07/durfmt),
[`timeago`](https://github.com/nripankadas07/timeago),
[`chronoparse`](https://github.com/nripankadas07/chronoparse),
[`crontab-lite`](https://github.com/nripankadas07/crontab-lite),
[`unitcalc`](https://github.com/nripankadas07/unitcalc),
[`semverlite`](https://github.com/nripankadas07/semverlite),
[`rangeset`](https://github.com/nripankadas07/rangeset).

### Strings and text

[`globmatch`](https://github.com/nripankadas07/globmatch) is the
most thoroughly tested matcher in here. It handles extglob,
POSIX character classes, the globstar (`**`), and parses to an
AST with a proper backtracking interpreter. Use it when
`fnmatch` isn't enough.

[`stringcase`](https://github.com/nripankadas07/stringcase) is
the case converter I always end up needing. Snake, camel,
pascal, kebab, constant, dot, title, path. All transitions work
both ways.

[`levendist`](https://github.com/nripankadas07/levendist),
[`wordwrap`](https://github.com/nripankadas07/wordwrap),
[`slugify-x`](https://github.com/nripankadas07/slugify-x),
[`expand`](https://github.com/nripankadas07/expand),
[`pathmask`](https://github.com/nripankadas07/pathmask),
[`pathmatch-ts`](https://github.com/nripankadas07/pathmatch-ts),
[`shell-quote`](https://github.com/nripankadas07/shell-quote),
[`shellexpand`](https://github.com/nripankadas07/shellexpand),
[`markdownlint`](https://github.com/nripankadas07/markdownlint),
[`pigeon`](https://github.com/nripankadas07/pigeon),
[`tinytemplate`](https://github.com/nripankadas07/tinytemplate),
[`tagged-template-ts`](https://github.com/nripankadas07/tagged-template-ts).

### Networking, IDs, hashing

[`cidrcalc`](https://github.com/nripankadas07/cidrcalc) does IPv4
CIDR math without importing `ipaddress`. Subnetting, aggregation,
membership tests, all of it.

[`digestlite`](https://github.com/nripankadas07/digestlite)
wraps the standard library's hash and HMAC primitives behind a
consistent streaming API. The `verify` function is
constant-time, which the docs for `hashlib` should mention but
don't.

[`uuidgen`](https://github.com/nripankadas07/uuidgen),
[`base62-ts`](https://github.com/nripankadas07/base62-ts),
[`colourdist`](https://github.com/nripankadas07/colourdist).

### Data structures

[`path-trie`](https://github.com/nripankadas07/path-trie),
[`bitvec`](https://github.com/nripankadas07/bitvec),
[`trie`](https://github.com/nripankadas07/trie),
[`trie-ts`](https://github.com/nripankadas07/trie-ts),
[`ringbuf`](https://github.com/nripankadas07/ringbuf),
[`flatdict`](https://github.com/nripankadas07/flatdict),
[`dotpath`](https://github.com/nripankadas07/dotpath),
[`chunkby`](https://github.com/nripankadas07/chunkby),
[`randpick`](https://github.com/nripankadas07/randpick),
[`strtable`](https://github.com/nripankadas07/strtable).

### Caches, retries, rate limits

[`tinycache`](https://github.com/nripankadas07/tinycache),
[`retryback`](https://github.com/nripankadas07/retryback),
[`tokenring-ts`](https://github.com/nripankadas07/tokenring-ts),
[`tsmemo`](https://github.com/nripankadas07/tsmemo),
[`lru-ts`](https://github.com/nripankadas07/lru-ts).

### Diff and config

[`diffstat`](https://github.com/nripankadas07/diffstat),
[`envdiff`](https://github.com/nripankadas07/envdiff),
[`jsonpatch-lite`](https://github.com/nripankadas07/jsonpatch-lite),
[`colortool`](https://github.com/nripankadas07/colortool).

### TypeScript building blocks

[`result-ts`](https://github.com/nripankadas07/result-ts) is a
`Result<T, E>` type with the combinators you actually use:
`map`, `flatMap`, `unwrap`, `all`, `any`, `partition`,
`tryCatch`, `fromPromise`, `fromNullable`. No clever monad
transformer plumbing — just the eight or nine functions that
matter.

[`eventbus-ts`](https://github.com/nripankadas07/eventbus-ts) is
a typed pub-sub bus with dotted topics and glob subscriptions
(`*`, `**`, `?`). Handler errors are isolated, dispatch uses a
snapshot, and subscribing during a dispatch doesn't get you a
spooky retroactive event.

[`tsparser`](https://github.com/nripankadas07/tsparser),
[`parseopts-ts`](https://github.com/nripankadas07/parseopts-ts),
[`argv-strict`](https://github.com/nripankadas07/argv-strict),
[`argv-zod`](https://github.com/nripankadas07/argv-zod),
[`decoder-ts`](https://github.com/nripankadas07/decoder-ts),
[`emitter-ts`](https://github.com/nripankadas07/emitter-ts).

### AI, product, and operations tools

[`agent-framework`](https://github.com/nripankadas07/agent-framework),
[`ai-toolkit`](https://github.com/nripankadas07/ai-toolkit),
[`api-mocker`](https://github.com/nripankadas07/api-mocker),
[`cli-timer`](https://github.com/nripankadas07/cli-timer),
[`config-loader`](https://github.com/nripankadas07/config-loader),
[`csv-explorer`](https://github.com/nripankadas07/csv-explorer),
[`dep-audit`](https://github.com/nripankadas07/dep-audit),
[`env-vault`](https://github.com/nripankadas07/env-vault),
[`feature-flags`](https://github.com/nripankadas07/feature-flags),
[`json-differ`](https://github.com/nripankadas07/json-differ),
[`log-parser`](https://github.com/nripankadas07/log-parser),
[`mlproject`](https://github.com/nripankadas07/mlproject),
[`prompt-eval`](https://github.com/nripankadas07/prompt-eval),
[`rag-pipeline`](https://github.com/nripankadas07/rag-pipeline),
[`rate-limiter`](https://github.com/nripankadas07/rate-limiter),
[`retry-lib`](https://github.com/nripankadas07/retry-lib),
[`schema-gen`](https://github.com/nripankadas07/schema-gen),
[`startup-dashboard`](https://github.com/nripankadas07/startup-dashboard),
[`task-queue`](https://github.com/nripankadas07/task-queue),
[`token-counter`](https://github.com/nripankadas07/token-counter).

## How to read these repos

Open any of them. The first sentence tells you what it does. The
second paragraph tells you what it doesn't do — that part is
usually more useful than the API reference. Then comes the
quick-start, then the full API surface, then the test
instructions.

The tests aren't an afterthought. Every public function has at
least a happy-path test, an edge-case test, and an error test.
Coverage numbers in the README are real; you can re-run them
yourself.

If you're evaluating my work and don't know where to start: try
[`tomlmini`](https://github.com/nripankadas07/tomlmini) for
real-format edge cases, [`safejson`](https://github.com/nripankadas07/safejson)
for hostile-input handling, [`decimal-ts`](https://github.com/nripankadas07/decimal-ts)
for exact arithmetic, or [`globmatch`](https://github.com/nripankadas07/globmatch)
for a parser with teeth.

## What's left

Twenty-one more projects. The remaining nights of the sprint are
spoken for in the queue file. Build log lives in the private
`forge-builds/` repo; the state files (`SOUL.md`, `MEMORY.md`,
`BUILD-LOG.md`, `CHRONICLE.md`) track every commit.

Built nightly. Tested ruthlessly. MIT licensed.
