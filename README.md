# Hi, I'm Nripanka 👋

I build small, sharp, dependency-free libraries — the kind of thing you reach
for when you don't want to pull in a 200-package transitive tree to do one
obvious job.

This profile is the home of a 60-night portfolio sprint: **two new
open-source projects every night**, each shipped with rigorous tests,
full type coverage, and a real README. So far: **62 / 120 projects**, all
built to the same bar.

---

## The bar

Every repository on this profile satisfies the same checklist:

- **TDD-built** — failing tests first, then minimum code to pass, then refactor.
- **100% line coverage** as a default, **100% branch coverage** for everything
  since Night 27. (No "this branch is unreachable" excuses — if it's truly
  unreachable, it gets deleted.)
- **`mypy --strict` / `tsc --strict` clean** — every public symbol typed,
  no `any` leaks, `py.typed` marker shipped on every Python package.
- **Functions ≤ 30 lines, nesting ≤ 3 levels** — verified by an AST walk
  before each push.
- **Zero runtime dependencies** unless absolutely required. Pure Python (or
  pure TypeScript) wherever possible.
- **MIT licensed.** **README with install / quick start / API reference /
  running tests** for every repo.

---

## The portfolio (62 repos)

### Parsing, codecs, and wire formats

[**`tomlmini`**](https://github.com/nripankadas07/tomlmini) — Zero-dep TOML v1.0
common-subset parser; values, tables, AoTs, inline tables, datetimes; rejects
ambiguous dotted-key edge cases.

[**`iniparse`**](https://github.com/nripankadas07/iniparse) — Zero-dep INI /
config parser with section inheritance and `${...}` interpolation.

[**`dotenv-mini`**](https://github.com/nripankadas07/dotenv-mini) — Strict,
predictable `.env` reader/writer; no `$VAR` interpolation, full quoting/escape
round-trip.

[**`querystring`**](https://github.com/nripankadas07/querystring) — Stable
encoder-configurable form-encoding with parse / serialize / merge / pick / omit.

[**`urltemplate`**](https://github.com/nripankadas07/urltemplate) — RFC 6570
URI Template expansion (levels 1-3), zero deps.

[**`mimedet`**](https://github.com/nripankadas07/mimedet) — Pure-Python MIME-type
detection from magic bytes (40+ formats), no `libmagic`.

[**`mimedb`**](https://github.com/nripankadas07/mimedb) — MIME-type ↔ extension
lookup (~190 baked-in types) with category classification, type/subtype
parsing, runtime-extensible registry.

[**`csvquote`**](https://github.com/nripankadas07/csvquote) — RFC-4180 CSV field
quoting/unquoting + single-line `split_row`, strict/lenient.

[**`csvtable`**](https://github.com/nripankadas07/csvtable) — Pretty-print
CSV/TSV (or any rows) as aligned ASCII / Unicode / Markdown / plain tables —
column-width inference, per-column align, 3-mode truncation, wide-char width.

[**`csvtail`**](https://github.com/nripankadas07/csvtail) — Streaming last-N
rows of a CSV/TSV in constant memory; hand-rolled state-machine parser handles
embedded newlines and CR/LF/CRLF.

[**`csvinfer`**](https://github.com/nripankadas07/csvinfer) — Infer CSV dialect
(delimiter, quote, header) from raw text without `csv.Sniffer`.

[**`mdtable`**](https://github.com/nripankadas07/mdtable) — Render GFM Markdown
tables from headers + rows with strict pipe escaping and per-column alignment.

[**`bencode`**](https://github.com/nripankadas07/bencode) — Strict,
dependency-free BitTorrent-style bencode encoder/decoder. Round-trips are
exact: rejects every non-canonical encoding.

[**`morse`**](https://github.com/nripankadas07/morse) — International Morse Code
encoder/decoder with prosigns and Farnsworth timing. Includes the classical
PARIS-derived inter-letter / inter-word gap formula.

### Encoding and binary

[**`hexdump`**](https://github.com/nripankadas07/hexdump) — Format bytes as
canonical hexdump output; round-trip parse back to bytes.

[**`hexstr`**](https://github.com/nripankadas07/hexstr) — Pack/unpack ints &
bytes into hex strings with prefixes, widths, sign modes, byte order.

[**`base62-ts`**](https://github.com/nripankadas07/base62-ts) — Base62
encoder/decoder for non-negative integers and byte arrays, custom alphabets.
*(TypeScript)*

[**`uuidgen`**](https://github.com/nripankadas07/uuidgen) — UUID v4/v5 batch
generator with base62 short form, strict parse, named namespace tables.

### Numbers, ranges, and time

[**`humanint`**](https://github.com/nripankadas07/humanint) — Parse and format
human-readable integers (`1.5k`, `2M`, `3.2B`).

[**`numparse`**](https://github.com/nripankadas07/numparse) — Forgiving parser
for loose numeric strings (`$1,234.56`, `1.5k`, `2 MiB`, `1h30m`, `12.5%`).

[**`numfmt`**](https://github.com/nripankadas07/numfmt) — Locale-free number
formatter (currency, percent, scientific).

[**`durfmt`**](https://github.com/nripankadas07/durfmt) — Format timedeltas and
numeric seconds as human durations (`1h 30m 12s`, `01:30:12`), zero deps.

[**`timeago`**](https://github.com/nripankadas07/timeago) — Human-readable
relative time formatting (`3 hours ago`, `in 2 days`).

[**`chronoparse`**](https://github.com/nripankadas07/chronoparse) —
Natural-language date/time parser, zero deps.

[**`crontab-lite`**](https://github.com/nripankadas07/crontab-lite) — Parse and
evaluate standard cron expressions, zero deps.

[**`unitcalc`**](https://github.com/nripankadas07/unitcalc) — Simple unit
conversion library (length, mass, temperature, time).

[**`semverlite`**](https://github.com/nripankadas07/semverlite) — Strict semver
parsing and comparison.

[**`rangeset`**](https://github.com/nripankadas07/rangeset) — Manage
non-overlapping integer ranges with set operations.

[**`randpick`**](https://github.com/nripankadas07/randpick) — Weighted random
sampling — Vose's alias method (O(1) per pick), cumulative-bisect, and
Efraimidis-Spirakis A-Res for sampling without replacement.

[**`colourdist`**](https://github.com/nripankadas07/colourdist) — CIE colour-
difference metrics (CIE76, CIE94, CIEDE2000) plus sRGB ↔ XYZ ↔ Lab conversions,
pure Python.

### Strings, search, and text

[**`stringcase`**](https://github.com/nripankadas07/stringcase) — Convert
strings between snake / camel / pascal / kebab / constant / dot / title /
path cases.

[**`slugify-x`**](https://github.com/nripankadas07/slugify-x) — Unicode-aware
URL slug generator.

[**`levendist`**](https://github.com/nripankadas07/levendist) — String distance
metrics: Levenshtein, Damerau-Levenshtein, Hamming, Jaro, Jaro-Winkler, LCS.

[**`wordwrap`**](https://github.com/nripankadas07/wordwrap) — ANSI-aware
paragraph wrap / fill / shorten with hanging indents and wide-character support.

[**`expand`**](https://github.com/nripankadas07/expand) — GNU-style tab-to-space
expansion + unexpand, custom tab stops, leading-only / all modes.

[**`globmatch`**](https://github.com/nripankadas07/globmatch) — fnmatch-
compatible matcher with extglob, POSIX classes, `**` globstar, AST +
backtracking interpreter.

[**`pathmask`**](https://github.com/nripankadas07/pathmask) — Glob-style path
matcher with negation and brace expansion.

[**`shell-quote`**](https://github.com/nripankadas07/shell-quote) —
Zero-dependency POSIX shell quoting, splitting, and safety checks.

[**`markdownlint`**](https://github.com/nripankadas07/markdownlint) — Validate
Markdown against common style rules.

[**`pigeon`**](https://github.com/nripankadas07/pigeon) — POSIX gettext-style
Plural-Forms parser/evaluator with built-in locale tables.

### Network and telephony

[**`cidrcalc`**](https://github.com/nripankadas07/cidrcalc) — IPv4 CIDR
arithmetic — parse, network/broadcast, membership, subnets, aggregate. No
`ipaddress` dep.

[**`phonenumber-mini`**](https://github.com/nripankadas07/phonenumber-mini) —
E.164 phone-number normalisation, zero deps, 50+ ITU country codes, no
`phonenumbers` dep.

### Data structures and iteration

[**`bitvec`**](https://github.com/nripankadas07/bitvec) — Compact bit vector
with set operations, slicing, and efficient storage.

[**`trie`**](https://github.com/nripankadas07/trie) — Trie (prefix tree) with
fast prefix search and autocomplete.

[**`ringbuf`**](https://github.com/nripankadas07/ringbuf) — Fixed-capacity ring
buffer with O(1) append, overwrite-oldest, indexable, reversible.

[**`flatdict`**](https://github.com/nripankadas07/flatdict) — Flatten /
unflatten nested dicts with dotted keys.

[**`strtable`**](https://github.com/nripankadas07/strtable) — Format tabular
data as aligned ASCII/Unicode tables.

[**`dotpath`**](https://github.com/nripankadas07/dotpath) — Dotted-key
get/set/has/del over nested dicts and lists, like `jq`'s path syntax minus
the language.

[**`chunkby`**](https://github.com/nripankadas07/chunkby) — Iterator helpers —
chunk by size, sliding windows, batch by predicate, partition, pairwise,
take/drop/nth, flatten.

### Caching, retry, async control

[**`tinycache`**](https://github.com/nripankadas07/tinycache) — Thread-safe
LRU + TTL cache decorator.

[**`retryback`**](https://github.com/nripankadas07/retryback) — Tiny retry
decorator with exponential backoff and jitter.

[**`tokenring-ts`**](https://github.com/nripankadas07/tokenring-ts) —
Token-bucket + leaky-bucket rate limiters with FIFO async consume and an
injectable clock for deterministic tests. *(TypeScript)*

[**`tsmemo`**](https://github.com/nripankadas07/tsmemo) — Type-safe memoize for
sync and async functions with TTL, LRU eviction, custom keys, and in-flight
call de-duplication. *(TypeScript)*

[**`emitter-ts`**](https://github.com/nripankadas07/emitter-ts) — Strict typed
event emitter with sync/async dispatch, once/off, and listener-error isolation.
*(TypeScript)*

### Validation and decoding

[**`decoder-ts`**](https://github.com/nripankadas07/decoder-ts) — Type-safe
runtime JSON validators built from composable decoder combinators.
*(TypeScript)*

### Diff, patch, and colours

[**`diffstat`**](https://github.com/nripankadas07/diffstat) — Compute unified
diff statistics (additions, deletions, changes).

[**`envdiff`**](https://github.com/nripankadas07/envdiff) — Compare two `.env`
files and report drift.

[**`jsonpatch-lite`**](https://github.com/nripankadas07/jsonpatch-lite) —
Minimal RFC-6902 JSON patch implementation.

[**`colortool`**](https://github.com/nripankadas07/colortool) — Convert and
manipulate colors across HEX / RGB / HSL.

### TypeScript developer experience

[**`tsparser`**](https://github.com/nripankadas07/tsparser) — Tiny TypeScript
tokenizer/parser for a subset of expressions.

[**`parseopts-ts`**](https://github.com/nripankadas07/parseopts-ts) — Zero-dep
argv parser: typed options, aliases, negatable booleans, arrays, choices,
`--` terminator, stop-at-positional.

[**`argv-strict`**](https://github.com/nripankadas07/argv-strict) — Strict
typed argv parser — every option has a typed schema; booleans never coerced
from strings.

---

## How to read these repos

Pick any project. The README opens with one sentence telling you what it does.
The next paragraph tells you what it doesn't do — the non-goals matter as
much as the surface area. Then quick start, then API reference, then running
tests.

Tests aren't an afterthought. Every public function has a happy-path test, an
edge-case test, and an error test. Coverage is reported in the README. The
type-checker (`mypy --strict` for Python, `tsc --strict` for TypeScript) is
part of the test gate.

If you're a recruiter or maintainer evaluating my work, the densest reads
are:

- [**`tomlmini`**](https://github.com/nripankadas07/tomlmini),
  [**`globmatch`**](https://github.com/nripankadas07/globmatch),
  [**`csvtable`**](https://github.com/nripankadas07/csvtable) — for handling
  real-world format edge cases.
- [**`bencode`**](https://github.com/nripankadas07/bencode) — for strict
  canonical-format validation.
- [**`levendist`**](https://github.com/nripankadas07/levendist),
  [**`colourdist`**](https://github.com/nripankadas07/colourdist),
  [**`randpick`**](https://github.com/nripankadas07/randpick) — for tight
  numeric work.
- [**`decoder-ts`**](https://github.com/nripankadas07/decoder-ts),
  [**`emitter-ts`**](https://github.com/nripankadas07/emitter-ts),
  [**`tsmemo`**](https://github.com/nripankadas07/tsmemo) — for generics-heavy
  TypeScript with `exactOptionalPropertyTypes` enabled.

---

## What's next

Nights 36-60 of the sprint will fill out the remaining 58 projects. Themes
on the upcoming list: a few more parsers (a TS-side bencode sibling, a
JSON-Patch generator that pairs with `jsonpatch-lite`, a strict ULID/KSUID
generator), a runtime number-theory library, a streaming-friendly JSON
streaming reader, and the flagship — `microbpe`, a from-scratch tokenizer
trainer with byte-pair-encoding semantics.

Build log lives in `forge-builds/` (private). State files (`SOUL.md`,
`MEMORY.md`, `BUILD-LOG.md`, `CHRONICLE.md`) track every commit night by
night.

---

*Built nightly. Tested ruthlessly. MIT licensed.*
