# Weekly reliability review — 4–10 October 2026

Observed 11 October 2026. Thirty launches on 4, 5, 6, 8, 9 and 10 October were reconciled against current public heads. The 7 October repair-only day remains a real 0/5 shortfall and is not filled by catch-up work.

## Install and demo reliability

All 30/30 current source sets passed fresh core tests, wheel build, new offline installation, installed examples and command success/error checks outside source on Linux Python 3.11. Code/fixtures were inspected and matched to current Git blobs before execution. First 15 installed examples use independent synthetic inputs or supplied fixtures; the latest 15 reuse their validated synthetic smoke contracts. Existing passing default-head CI and exact scope are in [workflow audit](WORKFLOW_AUDIT_2026-10-11.json); [weekly baseline and validation](WEEKLY_VALIDATION_2026-10-11.json) names every head. Other operating systems, all supported configuration combinations and every older pre-week repository install were not rerun.

Two initial independent harness mistakes were corrected against the real contract: plan-regression requires an EXPLAIN JSON Plan wrapper, and doc-anchor-audit intentionally accepts an omitted root. Correct fixtures passed; repository tests and implementation were not changed to hide errors. These were harness errors, not confirmed product failures.

## Genuine feedback and adoption evidence

Open and closed issue/PR records were read for all 30 repositories. No third-party report or PR was found in these accessible records. Repository metadata on 11 October reports zero stars and zero forks across this group. This is the first dated baseline here; no week-over-week trend is computed. Zero stars do not establish no user value. First-party traffic, downloads and unique installs are unavailable through the accessible connector; absence of those metrics is not evidence of absence of adoption. No stars or activity were manipulated.

## Maintenance burden and next briefs

19 critical Handlebars repairs from 9 October and the SQLite Python 3.10 rejection-normalization fix from 10 October remain linked dated history; all current heads and independent dependency audits pass within their stated coverage. No new confirmed code failure was found. [Historical critical repairs](HEALTH_REVIEW_2026-10-09.md); [SQLite repair](LAUNCHES_2026-10-10.md#confirmed-compatibility-error-repaired). A large repository portfolio still imposes recurring audit/installation and dependency-resolution work.

Future briefs should continue bounded input formats, strict malformed-input/resource limits, zero runtime dependencies where useful, early three-version installed-command CI, visible unsupported cases, and useful demo links. Broader standards and live-service integration should be added only with a concrete workflow and tests. Discovery remains descriptive topics and the profile index, without unsolicited promotion or promised organic growth. The 54 disabled Dependabot feeds, 153 missing CodeQL configurations and deployment inventory remain explicit coverage gaps, not silent successes.
