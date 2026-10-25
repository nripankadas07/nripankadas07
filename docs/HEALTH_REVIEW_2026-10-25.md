# Portfolio health and weekly review, 25 October 2026

Five original companion tools launched after their public source, remote CI and clean installation were verified. This review records observed checks and limits. It does not certify every possible configuration or unknown defect.

## Current account health

- Initial inventory and full default-head audit: 218/218 existing repositories. 781 checks succeeded, three configuration jobs were skipped, and no failed or pending current checks were found. All 300 current-head workflow runs inspected succeeded. No open issues or pull requests were found. Old failed runs superseded by passing current commits remain history.
- Final inventory: 223 owned public repositories, including the five below. Each new default commit passes both Python 3.11 and 3.13 CI jobs. Tests, compilation, wheel build, an installed console command outside the source tree and a dependency audit run in each job.
- Independent dependency coverage: 242 exact manifest/lock blobs in 217 existing applicable repositories, verified against fresh commit trees. All 27 npm scopes and 113 resolved Python pins pass. The five new pyproject files were verified byte-for-byte against their public commits, bringing manifest coverage to 247 files in 222 applicable repositories. Their combined fresh Python environment audit covered 27 packages with no known findings; each new project's remote environment audit also passes. mlproject has no applicable manifest.
- Security pages: 223/223 inspected. All 223 enabled secret feeds, 109 enabled Dependabot feeds and 10 enabled code-scanning feeds showed no open alerts. Dependabot is disabled in 114 repositories; code scanning needs setup in 213; all 223 malware feeds reported disabled. Disabled or unconfigured feeds are monitoring gaps, not successful scans. Settings were not changed.
- The public README, bio and six pinned descriptions contain no em dashes. The index introduction had stale dated coverage and has been corrected. Em dashes were removed from index descriptions while preserving their meaning. The three leading case studies, supporting projects, personal context, synthetic labels and AI-assistance disclosure remain intact.

## Repair completed during publication

The first Join Fanout Lab CI run passed tests and installation but failed its audit because the Python 3.11 runner included setuptools 79.0.1. The log reported PYSEC-2026-3447 and GHSA-xmj3-9gf7-h52w. CI now upgrades setuptools to 84.1 or newer and pip to 26.2 or newer before installing and auditing. Local verification used setuptools 84.2.1 and pip 26.2.2. The same correction is present in all five quickstarts and workflows. No vulnerability was ignored and no check was disabled.

[Original failing run](https://github.com/nripankadas07/join-fanout-lab/actions/runs/40170429499) remains available. The final passing run is linked below. Existing repositories needed no new repair today; yesterday's three dependency repairs remain verified history in the [24 October review](HEALTH_REVIEW_2026-10-24.md).

## Five launch receipts

All five public clones matched every expected SHA256 file digest, then passed unit/integration tests, wheel creation and clean installation. The real installed commands accepted their documented example and rejected malformed input from a temporary directory. There are 37 tests across the five suites; Join Fanout Lab also checks 144 seeded join-oracle cases. Examples use invented data.

| Project | Useful result | Verified public commit | Remote CI |
| --- | --- | --- | --- |
| [join-fanout-lab](https://github.com/nripankadas07/join-fanout-lab) | Predict Polars join row counts and explain the keys causing expansion. | [cf1b854](https://github.com/nripankadas07/join-fanout-lab/commit/cf1b85442d2d6357e2bf4d0d05d31fa8d720e541) | [Passing Python 3.11/3.13](https://github.com/nripankadas07/join-fanout-lab/actions/runs/40170745646) |
| [group-split-audit](https://github.com/nripankadas07/group-split-audit) | Find entity, fingerprint and declared time-window overlap between validation folds. | [80eb5f2](https://github.com/nripankadas07/group-split-audit/commit/80eb5f29bf15b75a8a6fb40ad069b4003ae575ff) | [Passing Python 3.11/3.13](https://github.com/nripankadas07/group-split-audit/actions/runs/40170776937) |
| [rootpath-rehearsal](https://github.com/nripankadas07/rootpath-rehearsal) | Rehearse public URL contracts in local FastAPI ASGI scenarios. | [a1ab230](https://github.com/nripankadas07/rootpath-rehearsal/commit/a1ab2305ced5bc8c25fa9c54a460c528978359fd) | [Passing Python 3.11/3.13](https://github.com/nripankadas07/rootpath-rehearsal/actions/runs/40170882214) |
| [compose-readiness-replay](https://github.com/nripankadas07/compose-readiness-replay) | Explain startup barriers from supplied Compose event evidence. | [1828b22](https://github.com/nripankadas07/compose-readiness-replay/commit/1828b22e34616123ffc06e8d9783a3c3b7e2053f) | [Passing Python 3.11/3.13](https://github.com/nripankadas07/compose-readiness-replay/actions/runs/40171066243) |
| [n8n-relocation-plan](https://github.com/nripankadas07/n8n-relocation-plan) | Review and apply offline metadata relocation plans; output workflows stay inactive. | [b65d59c](https://github.com/nripankadas07/n8n-relocation-plan/commit/b65d59c7a7e96554a5b72a586e466b48c2569511) | [Passing Python 3.11/3.13](https://github.com/nripankadas07/n8n-relocation-plan/actions/runs/40171097673) |

Each repository includes its candidate brief, dated research, alternatives, observed star counts, official documentation and issue evidence, license, realistic example, failure behavior and compatibility limits. Stars identify an audience, not demand or performance. No affiliation, endorsement, adoption or superiority is claimed.

Polars 2.0.0, scikit-learn 1.9.1 and FastAPI 0.162.0/HTTPX 0.28.1 were executed directly. Compose readiness uses documented semantics; Docker daemon interoperability was not executed. n8n relocation checks a pinned export metadata shape; n8n server import was not executed. The tools document these limits instead of claiming full upstream compatibility. HTML escaping and structure were tested; the cloud browser disallows local-file navigation, so a local visual rendering check was not performed or bypassed.

## Weekly review, 18 to 24 October

All 25 repositories created in the previous week passed fresh wheel builds, clean environment installation, real console help and their documented example outside the source tree. Their current default CI passed. No issue reports created that week were found. The 25 repositories had zero observed stars and forks at the 25 October baseline; traffic, repeat usage and private adoption evidence were unavailable. Zero stars do not establish lack of usefulness.

Narrow tasks, self-contained fixtures and working installed commands made the projects reproducible. The three development dependency repairs on 24 October show a real maintenance cost. Today's ecosystem dependencies were added only where the tool exercises an actual upstream API. Future selection should favor a specific user task, a realistic demonstration and manageable compatibility work. No attention or growth is promised.

## Remaining limits

Dependency findings reflect the current advisory databases and resolved versions. CI covers declared configurations; this was not a fresh installation of every historical repository on every operating system or deployment. Comprehensive deployment and traffic API coverage was unavailable. Disabled scanners remain explicit coverage gaps. New projects have independent CI dependency audits even where GitHub Dependabot is disabled. No account-wide claim of being error-free is made.

[Project index](PROJECT_INDEX.md) · [Previous review](HEALTH_REVIEW_2026-10-24.md)
