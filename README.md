# Hi, I'm Nripanka 👋

I build small, sharp, dependency-free libraries — the kind of thing
you reach for when you don't want to pull in a 200-package transitive
tree to do one obvious job.

This profile is the home of a 60-night portfolio sprint: **two new
open-source projects every night**, each shipped with rigorous tests,
full type coverage, and a real README. So far: **78 / 120 projects**,
all built to the same bar.

---

## The bar

Every repository on this profile satisfies the same checklist:

- **TDD-built** — failing tests first, then minimum code to pass,
  then refactor.
- **100% line coverage** as a default, **100% branch coverage** for
  everything since Night 27. (No "this branch is unreachable"
  excuses — if it's truly unreachable, it gets deleted.)
- **`mypy --strict` clean** (Python) / **`tsc --strict --noEmit`
  clean with the full strictness panel** (TypeScript) — every public
  symbol typed, no `Any` leaks, `py.typed` marker shipped.
- **Functions ≤ 30 lines, nesting ≤ 3 levels** — verified by an AST
  walk before each push.
- **Zero runtime dependencies** unless absolutely required. Pure
  Python (or pure TypeScript) wherever possible.
- **MIT licensed**. **README with install / quick start / API
  reference / running tests** for every repo.

---

## The portfolio

### Parsers, codecs, and wire formats

[**`bencode`**](https://github.com/nripankadas07/bencode) — Strict,
dependency-free BitTorrent-style bencode encoder/decoder. Round-trips
are exact: rejects every non-canonical encoding (leading zeros,
`i-0e`, dict keys out of order or duplicated, trailing data).

[**`morse`**](https://github.com/nripankadas07/morse) — International
Morse Code encoder/decoder with prosigns and Farnsworth timing.
Includes the classical PARIS-derived formula for inter-letter /
inter-word gap durations.

[**`tomlmini`**](https://github.com/nripankadas07/tomlmini) —
Zero-dependency TOML v1.0 common-subset parser. Handles values,
tables, AoTs, inline tables, datetimes; rejects ambiguous dotted-key
edge cases.

[**`iniparse`**](https://github.com/nripankadas07/iniparse) —
Zero-dep INI / config parser with section inheritance and `${...}`
interpolation.

[**`querystring`**](https://github.com/nripankadas07/querystring) —
Stable encoder-configurable form-encoding with parse / serialize /
merge / pick / omit.

[**`urltemplate`**](https://github.com/nripankadas07/urltemplate) —
RFC 6570 URI Template expansion (levels 1–3), zero deps.

[**`csvquote`**](https://github.com/nripankadas07/csvquote) —
RFC-4180 CSV field quoting/unquoting + single-line `split_row`,
strict/lenient.

[**`csvtable`**](https://github.com/nripankadas07/csvtable) —
Pretty-print CSV/TSV (or any rows) as aligned ASCII / Unicode /
Markdown / plain tables — column-width inference, per-column align,
3-mode truncation, wide-char width.

[**`csvtail`**](https://github.com/nripankadas07/csvtail) — Streaming
last-N rows of a CSV/TSV in constant memory; hand-rolled
state-machine parser handles embedded newlines and CR/LF/CRLF.

[**`csvinfer`**](https://github.com/nripankadas07/csvinfer) — Infer
CSV dialect (delimiter, quote, header) from raw text without
`csv.Sniffer`.

[**`mdtable`**](https://github.com/nripankadas07/mdtable) — Render
GFM Markdown tables from headers + rows with strict pipe escaping
and per-column alignment.

[**`dotenv-mini`**](https://github.com/nripankadas07/dotenv-mini) —
Strict, predictable `.env` reader/writer; no `$VAR` interpolation,
full quoting/escape round-trip.

[**`hexdump`**](https://github.com/nripankadas07/hexdump) — Format
bytes as canonical hexdump output; round-trip parse back to bytes.

[**`hexstr`**](https://github.com/nripankadas07/hexstr) — Pack/unpack
ints & bytes into hex strings with prefixes, widths, sign modes,
byte order.

[**`iso8601`**](https://github.com/nripankadas07/iso8601) — Strict
ISO-8601 date / time / datetime / duration parser with timezone
offsets, calendar / ordinal / week-date forms, fractional seconds,
and round-trip formatters.

[**`urlnorm`**](https://github.com/nripankadas07/urlnorm) — Zero-dep
URL normalizer: case-fold, default-port strip, dot-segment removal,
percent-encoding canonicalization, optional query sort.

[**`jsonptr`**](https://github.com/nripankadas07/jsonptr) — Zero-dep
RFC 6901 JSON Pointer: parse / format / escape / resolve / get / has
/ set / remove on nested dicts and lists, with a clean error tree.

[**`safejson`**](https://github.com/nripankadas07/safejson) — Hardened
JSON parser: configurable depth/size limits, duplicate-key detection,
NaN/Infinity rejection, type whitelisting, allocation-free streaming
pre-scan. Defeats the `RecursionError` class of attack on
`json.loads`.

[**`mimedet`**](https://github.com/nripankadas07/mimedet) — Pure-Python
MIME-type detection from magic bytes (40+ formats), no libmagic.

[**`mimedb`**](https://github.com/nripankadas07/mimedb) — MIME-type
↔ extension lookup with category classification, type/subtype
parsing, and a runtime-extensible registry.

[**`phonenumber-mini`**](https://github.com/nripankadas07/phonenumber-mini) —
E.164 phone-number normalisation, zero deps, 50+ ITU country codes,
no `phonenumbers` dep.

### Numbers, ranges, and time

[**`humanint`**](https://github.com/nripankadas07/humanint) — Parse
and format human-readable integers (`1.5k`, `2M`, `3.2B`).

[**`numparse`**](https://github.com/nripankadas07/numparse) —
Forgiving parser for loose numeric strings (`$1,234.56`, `1.5k`,
`2 MiB`, `1h30m`, `12.5%`).

[**`numfmt`**](https://github.com/nripankadas07/numfmt) — Locale-free
number formatter (currency, percent, scientific).

[**`durfmt`**](https://github.com/nripankadas07/durfmt) — Format
timedeltas and numeric seconds as human durations (`1h 30m 12s`,
`01:30:12`), zero deps.

[**`timeago`**](https://github.com/nripankadas07/timeago) —
Human-readable relative time formatting (`3 hours ago`,
`in 2 days`).

[**`chronoparse`**](https://github.com/nripankadas07/chronoparse) —
Natural-language date/time parser, zero deps.

[**`crontab-lite`**](https://github.com/nripankadas07/crontab-lite) —
Parse and evaluate standard cron expressions, zero deps.

[**`unitcalc`**](https://github.com/nripankadas07/unitcalc) — Simple
unit conversion library (length, mass, temperature, time).

[**`semverlite`**](https://github.com/nripankadas07/semverlite) —
Strict semver parsing and comparison.

[**`rangeset`**](https://github.com/nripankadas07/rangeset) — Manage
non-overlapping integer ranges with set operations.

[**`numbertheory`**](https://github.com/nripankadas07/numbertheory) —
Pure-Python number-theory helpers: gcd/lcm, extended Euclid, modular
inverse, Miller-Rabin primality, factorisation, Euler phi, Möbius,
CRT, Jacobi/Legendre.

[**`decimal-ts`**](https://github.com/nripankadas07/decimal-ts) —
Arbitrary-precision fixed-point decimal arithmetic on BigInt; seven
rounding modes, immutable, exact `0.1 + 0.2`, zero deps.
*(TypeScript)*

### Strings, search, and text

[**`stringcase`**](https://github.com/nripankadas07/stringcase) —
Convert strings between snake / camel / pascal / kebab / constant /
dot / title / path cases.

[**`slugify-x`**](https://github.com/nripankadas07/slugify-x) —
Unicode-aware URL slug generator.

[**`levendist`**](https://github.com/nripankadas07/levendist) —
String distance metrics: Levenshtein, Damerau-Levenshtein, Hamming,
Jaro, Jaro-Winkler, LCS.

[**`wordwrap`**](https://github.com/nripankadas07/wordwrap) —
ANSI-aware paragraph wrap / fill / shorten with hanging indents and
wide-character support.

[**`expand`**](https://github.com/nripankadas07/expand) — GNU-style
tab-to-space expansion + unexpand, custom tab stops, leading-only /
all modes.

[**`globmatch`**](https://github.com/nripankadas07/globmatch) —
fnmatch-compatible matcher with extglob, POSIX classes, `**`
globstar, AST + backtracking interpreter.

[**`pathmask`**](https://github.com/nripankadas07/pathmask) —
Glob-style path matcher with negation and brace expansion.

[**`pathmatch-ts`**](https://github.com/nripankadas07/pathmatch-ts) —
Typed glob/path matcher with brace expansion, globstar, character
classes, case-insensitive and dot-file modes, and a pre-compilable
`PathMatcher`. *(TypeScript)*

[**`shell-quote`**](https://github.com/nripankadas07/shell-quote) —
Zero-dependency POSIX shell quoting, splitting, and safety checks.

[**`shellexpand`**](https://github.com/nripankadas07/shellexpand) —
Zero-dep POSIX-style shell text expansion: tilde, brace, parameter
(`$VAR`, `${VAR:-d}`) with escape handling and a clean error tree.

[**`markdownlint`**](https://github.com/nripankadas07/markdownlint) —
Validate Markdown against common style rules.

[**`pigeon`**](https://github.com/nripankadas07/pigeon) — POSIX
gettext-style Plural-Forms parser/evaluator with built-in locale
tables.

[**`tinytemplate`**](https://github.com/nripankadas07/tinytemplate) —
Zero-dep `${name}` template renderer with defaults, dotted-path
access, and a small filter chain.

[**`tagged-template-ts`**](https://github.com/nripankadas07/tagged-template-ts) —
Type-safe tagged-template helpers: html, sql, dedent, oneline, raw,
regex, urlPath, csv, plus a `tag()` factory. *(TypeScript)*

### Networks, IDs, and crypto

[**`cidrcalc`**](https://github.com/nripankadas07/cidrcalc) — IPv4
CIDR arithmetic — parse, network/broadcast, membership, subnets,
aggregate. No `ipaddress` dep.

[**`uuidgen`**](https://github.com/nripankadas07/uuidgen) — UUID v4/v5
batch generator with base62 short form, strict parse, named namespace
tables.

[**`base62-ts`**](https://github.com/nripankadas07/base62-ts) —
Base62 encoder/decoder for non-negative integers and byte arrays,
custom alphabets. *(TypeScript)*

[**`digestlite`**](https://github.com/nripankadas07/digestlite) —
Zero-dep wrapper unifying SHA-1/256/512 + HMAC + base32/64 with a
streaming `Hasher`/`Hmac` API, alias-tolerant resolution, and
constant-time `verify`.

[**`colourdist`**](https://github.com/nripankadas07/colourdist) — CIE
colour-difference metrics (CIE76, CIE94, CIEDE2000) plus sRGB ↔ XYZ
↔ Lab conversions, pure Python.

### Data structures and iteration

[**`bitvec`**](https://github.com/nripankadas07/bitvec) — Compact bit
vector with set operations, slicing, and efficient storage.

[**`trie`**](https://github.com/nripankadas07/trie) — Trie (prefix
tree) with fast prefix search and autocomplete.

[**`trie-ts`**](https://github.com/nripankadas07/trie-ts) — Type-safe
Trie (prefix tree) with autocomplete, longest-prefix matching,
deletion with leaf pruning, and lexicographic iteration.
*(TypeScript)*

[**`ringbuf`**](https://github.com/nripankadas07/ringbuf) —
Fixed-capacity ring buffer with O(1) append, overwrite-oldest,
indexable, reversible.

[**`flatdict`**](https://github.com/nripankadas07/flatdict) —
Flatten / unflatten nested dicts with dotted keys.

[**`dotpath`**](https://github.com/nripankadas07/dotpath) —
Dotted-key get/set/has/del over nested dicts and lists, like jq's
path syntax minus the language.

[**`chunkby`**](https://github.com/nripankadas07/chunkby) — Iterator
helpers: chunk by size, sliding windows, batch by predicate,
partition, pairwise, take/drop/nth, flatten.

[**`randpick`**](https://github.com/nripankadas07/randpick) —
Weighted random sampling helpers — Vose's alias method,
cumulative-bisect, Efraimidis-Spirakis A-Res.

[**`strtable`**](https://github.com/nripankadas07/strtable) — Format
tabular data as aligned ASCII/Unicode tables.

### Decorators, caches, and rate limiting

[**`tinycache`**](https://github.com/nripankadas07/tinycache) —
Thread-safe LRU + TTL cache decorator.

[**`retryback`**](https://github.com/nripankadas07/retryback) — Tiny
retry decorator with exponential backoff and jitter.

[**`tokenring-ts`**](https://github.com/nripankadas07/tokenring-ts) —
Token-bucket + leaky-bucket rate limiters with FIFO async consume
and an injectable clock for deterministic tests. *(TypeScript)*

[**`tsmemo`**](https://github.com/nripankadas07/tsmemo) — Type-safe
memoize for sync and async functions with TTL, LRU eviction, custom
keys, and in-flight call de-duplication. *(TypeScript)*

[**`lru-ts`**](https://github.com/nripankadas07/lru-ts) — Type-safe
LRU cache with optional TTL, capacity / TTL / manual / replace /
clear eviction reasons, injectable `Clock`, runtime stats, and
resize. *(TypeScript)*

### Diff, patch, and config drift

[**`diffstat`**](https://github.com/nripankadas07/diffstat) — Compute
unified diff statistics (additions, deletions, changes).

[**`envdiff`**](https://github.com/nripankadas07/envdiff) — Compare
two `.env` files and report drift.

[**`jsonpatch-lite`**](https://github.com/nripankadas07/jsonpatch-lite) —
Minimal RFC-6902 JSON patch implementation.

[**`colortool`**](https://github.com/nripankadas07/colortool) —
Convert and manipulate colors across HEX / RGB / HSL.

### Functional / type-safe TypeScript

[**`tsparser`**](https://github.com/nripankadas07/tsparser) — Tiny
TypeScript tokenizer/parser for a subset of expressions.

[**`parseopts-ts`**](https://github.com/nripankadas07/parseopts-ts) —
Zero-dep argv parser: typed options, aliases, negatable booleans,
arrays, choices, `--` terminator, stop-at-positional.

[**`argv-strict`**](https://github.com/nripankadas07/argv-strict) —
Strict typed argv parser; every option has a typed schema; booleans
never coerced from strings.

[**`argv-zod`**](https://github.com/nripankadas07/argv-zod) —
Type-safe argv parser with a Zod-style fluent schema builder;
inferred result types, env fallbacks, aliases, defaults.

[**`decoder-ts`**](https://github.com/nripankadas07/decoder-ts) —
Type-safe runtime JSON validators built from composable decoder
combinators.

[**`emitter-ts`**](https://github.com/nripankadas07/emitter-ts) —
Strict typed event emitter with sync/async dispatch, once/off, and
listener-error isolation.

[**`eventbus-ts`**](https://github.com/nripankadas07/eventbus-ts) —
Type-safe pub-sub bus with dotted topics and `*` / `**` / `?` glob
subscriptions, handler-error isolation, snapshot dispatch.

[**`result-ts`**](https://github.com/nripankadas07/result-ts) —
Type-safe `Result<T, E>` with map / flatMap / unwrap / all / any /
partition / tryCatch / fromPromise / fromNullable combinators.

---

## How to read these repos

Pick any project. The README starts with one sentence telling you
what it does. The next paragraph tells you what it doesn't do — the
non-goals matter as much as the surface area. Then quick start, then
API reference, then running tests.

Tests are not an afterthought. Every public function has a
happy-path test, an edge-case test, and an error test. Coverage is
reported in the README. `mypy --strict` (Python) or
`tsc --strict --noEmit` (TypeScript) is part of the test gate.

If you're a recruiter or a maintainer evaluating my work: open
[`tomlmini`](https://github.com/nripankadas07/tomlmini),
[`globmatch`](https://github.com/nripankadas07/globmatch), or
[`csvtable`](https://github.com/nripankadas07/csvtable) for a sense
of how I handle real-format edge cases. Open
[`bencode`](https://github.com/nripankadas07/bencode) for strict
canonical-format validation. Open
[`safejson`](https://github.com/nripankadas07/safejson) for hardened
parsing under hostile input. Open
[`decimal-ts`](https://github.com/nripankadas07/decimal-ts) for
exact arithmetic on `bigint`.

---

## What's next

Nights 44–60 of the sprint will fill out the remaining 42 projects.
Build log lives in `forge-builds/` (private). State files
(`SOUL.md`, `MEMORY.md`, `BUILD-LOG.md`, `CHRONICLE.md`) track every
commit night-by-night.

---

*Built nightly. Tested ruthlessly. MIT licensed.*
