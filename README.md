# Hi, I'm Nripanka 👋

I build small, sharp, dependency-free libraries — the kind of thing you reach for when you don't want to pull in a 200-package transitive tree to do one obvious job.

This profile is the home of a 60-night portfolio sprint: **two new open-source projects every night**, each shipped with rigorous tests, full type coverage, and a real README. So far: **52 / 112 projects**, all built to the same bar.

---

## The bar

Every repository on this profile satisfies the same checklist:

- **TDD-built** — failing tests first, then minimum code to pass, then refactor.
- **100% line coverage** as a default, **100% branch coverage** for everything since Night 27. (No "this branch is unreachable" excuses — if it's truly unreachable, it gets deleted.)
- **`mypy --strict` clean** — every public symbol typed, no `Any` leaks, `py.typed` marker shipped.
- **Functions ≤ 30 lines, nesting ≤ 3 levels** — verified by an AST walk before each push.
- **Zero runtime dependencies** unless absolutely required. Pure Python (or pure TypeScript) wherever possible.
- **MIT licensed**. **README with install / quick start / API reference / running tests** for every repo.

---

## The portfolio

### Parsers, codecs, and wire formats

[**`bencode`**](https://github.com/nripankadas07/bencode) — Strict, dependency-free BitTorrent-style bencode encoder/decoder. Round-trips are exact: rejects every non-canonical encoding (leading zeros, `i-0e`, dict keys out of order or duplicated, trailing data).

[**`morse`**](https://github.com/nripankadas07/morse) — International Morse Code encoder/decoder with prosigns and Farnsworth timing. Includes the classical PARIS-derived formula for inter-letter / inter-word gap durations.

[**`tomlmini`**](https://github.com/nripankadas07/tomlmini) — Zero-dependency TOML v1.0 common-subset parser. Handles values, tables, AoTs, inline tables, datetimes; rejects ambiguous dotted-key edge cases.

[**`iniparse`**](https://github.com/nripankadas07/iniparse) — Zero-dep INI / config parser with section inheritance and `${...}` interpolation.

[**`querystring`**](https://github.com/nripankadas07/querystring) — Stable encoder-configurable form-encoding with parse / serialize / merge / pick / omit.

[**`urltemplate`**](https://github.com/nripankadas07/urltemplate) — RFC 6570 URI Template expansion (levels 1-3), zero deps.

[**`csvquote`**](https://github.com/nripankadas07/csvquote) — RFC-4180 CSV field quoting/unquoting + single-line `split_row`, strict/lenient.

[**`csvtable`**](https://github.com/nripankadas07/csvtable) — Pretty-print CSV/TSV (or any rows) as aligned ASCII / Unicode / Markdown / plain tables — column-width inference, per-column align, 3-mode truncation, wide-char width.

[**`mdtable`**](https://github.com/nripankadas07/mdtable) — Render GFM Markdown tables from headers + rows with strict pipe escaping and per-column alignment.

[**`dotenv-mini`**](https://github.com/nripankadas07/dotenv-mini) — Strict, predictable `.env` reader/writer; no `$VAR` interpolation, full quoting/escape round-trip.

[**`hexdump`**](https://github.com/nripankadas07/hexdump) — Format bytes as canonical hexdump output; round-trip parse back to bytes.

[**`hexstr`**](https://github.com/nripankadas07/hexstr) — Pack/unpack ints & bytes into hex strings with prefixes, widths, sign modes, byte order.

### Numbers, ranges, and time

[**`humanint`**](https://github.com/nripankadas07/humanint) — Parse and format human-readable integers (`1.5k`, `2M`, `3.2B`).

[**`numparse`**](https://github.com/nripankadas07/numparse) — Forgiving parser for loose numeric strings (`$1,234.56`, `1.5k`, `2 MiB`, `1h30m`, `12.5%`).

[**`numfmt`**](https://github.com/nripankadas07/numfmt) — Locale-free number formatter (currency, percent, scientific).

[**`durfmt`**](https://github.com/nripankadas07/durfmt) — Format timedeltas and numeric seconds as human durations (`1h 30m 12s`, `01:30:12`), zero deps.

[**`timeago`**](https://github.com/nripankadas07/timeago) — Human-readable relative time formatting (`3 hours ago`, `in 2 days`).

[**`chronoparse`**](https://github.com/nripankadas07/chronoparse) — Natural-language date/time parser, zero deps.

[**`crontab-lite`**](https://github.com/nripankadas07/crontab-lite) — Parse and evaluate standard cron expressions, zero deps.

[**`unitcalc`**](https://github.com/nripankadas07/unitcalc) — Simple unit conversion library (length, mass, temperature, time).

[**`semverlite`**](https://github.com/nripankadas07/semverlite) — Strict semver parsing and comparison.

[**`rangeset`**](https://github.com/nripankadas07/rangeset) — Manage non-overlapping integer ranges with set operations.

### Strings, search, and text

[**`stringcase`**](https://github.com/nripankadas07/stringcase) — Convert strings between snake / camel / pascal / kebab / constant / dot / title / path cases.

[**`slugify-x`**](https://github.com/nripankadas07/slugify-x) — Unicode-aware URL slug generator.

[**`levendist`**](https://github.com/nripankadas07/levendist) — String distance metrics: Levenshtein, Damerau-Levenshtein, Hamming, Jaro, Jaro-Winkler, LCS.

[**`wordwrap`**](https://github.com/nripankadas07/wordwrap) — ANSI-aware paragraph wrap / fill / shorten with hanging indents and wide-character support.

[**`expand`**](https://github.com/nripankadas07/expand) — GNU-style tab-to-space expansion + unexpand, custom tab stops, leading-only / all modes.

[**`globmatch`**](https://github.com/nripankadas07/globmatch) — fnmatch-compatible matcher with extglob, POSIX classes, `**` globstar, AST + backtracking interpreter.

[**`pathmask`**](https://github.com/nripankadas07/pathmask) — Glob-style path matcher with negation and brace expansion.

[**`shell-quote`**](https://github.com/nripankadas07/shell-quote) — Zero-dependency POSIX shell quoting, splitting, and safety checks.

[**`markdownlint`**](https://github.com/nripankadas07/markdownlint) — Validate Markdown against common style rules.

[**`pigeon`**](https://github.com/nripankadas07/pigeon) — POSIX gettext-style Plural-Forms parser/evaluator with built-in locale tables.

### Networks, IDs, and crypto-ish

[**`cidrcalc`**](https://github.com/nripankadas07/cidrcalc) — IPv4 CIDR arithmetic — parse, network/broadcast, membership, subnets, aggregate. No `ipaddress` dep.

[**`uuidgen`**](https://github.com/nripankadas07/uuidgen) — UUID v4/v5 batch generator with base62 short form, strict parse, named namespace tables.

[**`base62-ts`**](https://github.com/nripankadas07/base62-ts) — Base62 encoder/decoder for non-negative integers and byte arrays, custom alphabets. *(TypeScript)*

### Data structures and iteration

[**`bitvec`**](https://github.com/nripankadas07/bitvec) — Compact bit vector with set operations, slicing, and efficient storage.

[**`trie`**](https://github.com/nripankadas07/trie) — Trie (prefix tree) with fast prefix search and autocomplete.

[**`ringbuf`**](https://github.com/nripankadas07/ringbuf) — Fixed-capacity ring buffer with O(1) append, overwrite-oldest, indexable, reversible.

[**`flatdict`**](https://github.com/nripankadas07/flatdict) — Flatten / unflatten nested dicts with dotted keys.

[**`strtable`**](https://github.com/nripankadas07/strtable) — Format tabular data as aligned ASCII/Unicode tables.

### Decorators, retries, and caches

[**`tinycache`**](https://github.com/nripankadas07/tinycache) — Thread-safe LRU + TTL cache decorator.

[**`retryback`**](https://github.com/nripankadas07/retryback) — Tiny retry decorator with exponential backoff and jitter.

### Diff, patch, and config drift

[**`diffstat`**](https://github.com/nripankadas07/diffstat) — Compute unified diff statistics (additions, deletions, changes).

[**`envdiff`**](https://github.com/nripankadas07/envdiff) — Compare two `.env` files and report drift.

[**`jsonpatch-lite`**](https://github.com/nripankadas07/jsonpatch-lite) — Minimal RFC-6902 JSON patch implementation.

[**`colortool`**](https://github.com/nripankadas07/colortool) — Convert and manipulate colors across HEX / RGB / HSL.

### TypeScript

[**`tsparser`**](https://github.com/nripankadas07/tsparser) — Tiny TypeScript tokenizer/parser for a subset of expressions.

[**`parseopts-ts`**](https://github.com/nripankadas07/parseopts-ts) — Zero-dep argv parser: typed options, aliases, negatable booleans, arrays, choices, `--` terminator, stop-at-positional.

---

## How to read these repos

Pick any project. The README starts with one sentence telling you what it does. The next paragraph tells you what it doesn't do — the non-goals matter as much as the surface area. Then quick start, then API reference, then running tests.

Tests are not an afterthought. Every public function has a happy-path test, an edge-case test, and an error test. Coverage is reported in the README. mypy `--strict` is part of the test gate.

If you're a recruiter or a maintainer evaluating my work: open [`tomlmini`](https://github.com/nripankadas07/tomlmini), [`globmatch`](https://github.com/nripankadas07/globmatch), or [`csvtable`](https://github.com/nripankadas07/csvtable) for a sense of how I handle real-format edge cases. Open [`bencode`](https://github.com/nripankadas07/bencode) for an example of strict canonical-format validation. Open [`levendist`](https://github.com/nripankadas07/levendist) for tight numeric work.

---

## What's next

Nights 31–60 of the sprint will fill out the remaining 60 projects: argv-strict (a stricter parseopts), emitter-ts (typed event emitter), bencode's TS sibling, phone-number normalization, color-difference metrics (CIE76/94/2000), a few more parsers, and a flagship — `microbpe`, a from-scratch tokenizer trainer with byte-pair-encoding semantics.

Build log lives in `forge-builds/` (private). State files (`SOUL.md`, `MEMORY.md`, `BUILD-LOG.md`, `CHRONICLE.md`) track every commit night-by-night.

---

*Built nightly. Tested ruthlessly. MIT licensed.*
