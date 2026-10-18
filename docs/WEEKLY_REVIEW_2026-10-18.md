# Weekly reliability review —18 October2026

Scope: all35 launches from11–17 October at freshly read current public commits. This is a new Linux/Python 3.12 retest, separate from the historical release CI matrices.

## Install and demo reliability

All35 passed source behavior tests, compilation, wheel construction, fresh-venv installation, installed console help, documented example and meaningful failure checks outside the checkout. Source, examples, package metadata and licenses were fetched from the recorded commits and independently Git-blob verified. No repository scripts were executed merely to discover manifests. Binary examples were invented inputs.

| Project | Current tested commit | Fresh install/examples | Stars / forks observed18 October |
| --- | --- | --- | --- |
| [accept-media-witness](https://github.com/nripankadas07/accept-media-witness) | [`f3ba0c8371aa`](https://github.com/nripankadas07/accept-media-witness/commit/f3ba0c8371aa1de81cf7af44f2dd815d2902ed8b) | PASSED | 0 / 0 |
| [backup-chain-audit](https://github.com/nripankadas07/backup-chain-audit) | [`7ad61fb576c1`](https://github.com/nripankadas07/backup-chain-audit/commit/7ad61fb576c10679a216b90bfa58336ddd07bbbe) | PASSED | 0 / 0 |
| [bom-rollup-ledger](https://github.com/nripankadas07/bom-rollup-ledger) | [`e0f55ab13f50`](https://github.com/nripankadas07/bom-rollup-ledger/commit/e0f55ab13f50f909147a768089fbbc105f70e658) | PASSED | 0 / 0 |
| [capacity-cut-report](https://github.com/nripankadas07/capacity-cut-report) | [`13fc7e7d13c2`](https://github.com/nripankadas07/capacity-cut-report/commit/13fc7e7d13c2ed9832ed64ccc57e8247d7f44c9c) | PASSED | 0 / 0 |
| [clock-quorum-window](https://github.com/nripankadas07/clock-quorum-window) | [`35552da4863c`](https://github.com/nripankadas07/clock-quorum-window/commit/35552da4863cc420666f3226336eb1af6c60bed6) | PASSED | 0 / 0 |
| [cookie-scope-witness](https://github.com/nripankadas07/cookie-scope-witness) | [`8a020e25d9e3`](https://github.com/nripankadas07/cookie-scope-witness/commit/8a020e25d9e385324f4ca4376a7ad41b88a20364) | PASSED | 0 / 0 |
| [cron-dst-witness](https://github.com/nripankadas07/cron-dst-witness) | [`ef0e0516fdb8`](https://github.com/nripankadas07/cron-dst-witness/commit/ef0e0516fdb8d5f855ade9eaebb33535cbc5d7fb) | PASSED | 0 / 0 |
| [cue-sample-plan](https://github.com/nripankadas07/cue-sample-plan) | [`094762d93f18`](https://github.com/nripankadas07/cue-sample-plan/commit/094762d93f180656f4aac9d7b50e99938a4b058f) | PASSED | 0 / 0 |
| [dns-serial-quorum](https://github.com/nripankadas07/dns-serial-quorum) | [`434e9e0d2ca1`](https://github.com/nripankadas07/dns-serial-quorum/commit/434e9e0d2ca15b8852959a0241982b46633906b6) | PASSED | 0 / 0 |
| [font-coverage-plan](https://github.com/nripankadas07/font-coverage-plan) | [`e00b83b25938`](https://github.com/nripankadas07/font-coverage-plan/commit/e00b83b259386c3f135093f00ae0a415b65de808) | PASSED | 0 / 0 |
| [git-ref-retention](https://github.com/nripankadas07/git-ref-retention) | [`ecc37b610226`](https://github.com/nripankadas07/git-ref-retention/commit/ecc37b6102263670c1c5ea9ed9806d80067e0b6e) | PASSED | 0 / 0 |
| [gpx-dwell-report](https://github.com/nripankadas07/gpx-dwell-report) | [`ecc29385b74f`](https://github.com/nripankadas07/gpx-dwell-report/commit/ecc29385b74f3bf547fb2e6d5337dcef77425f29) | PASSED | 0 / 0 |
| [http-range-witness](https://github.com/nripankadas07/http-range-witness) | [`36fbb1da74db`](https://github.com/nripankadas07/http-range-witness/commit/36fbb1da74db1dc338f4baf56213caaab20a4e38) | PASSED | 0 / 0 |
| [invoice-rounding-ledger](https://github.com/nripankadas07/invoice-rounding-ledger) | [`e2abf8c90a77`](https://github.com/nripankadas07/invoice-rounding-ledger/commit/e2abf8c90a77b894ba6c33da0b22789e89db27ce) | PASSED | 0 / 0 |
| [kafka-offset-audit](https://github.com/nripankadas07/kafka-offset-audit) | [`418d391468ee`](https://github.com/nripankadas07/kafka-offset-audit/commit/418d391468ee02fe6a12d0732557ecc76e51f94f) | PASSED | 0 / 0 |
| [matrix-include-trace](https://github.com/nripankadas07/matrix-include-trace) | [`ce5c54435ff3`](https://github.com/nripankadas07/matrix-include-trace/commit/ce5c54435ff3f26a6ccd533e1e0d36c26dd134df) | PASSED | 0 / 0 |
| [modbus-frame-ledger](https://github.com/nripankadas07/modbus-frame-ledger) | [`19cf250a7c17`](https://github.com/nripankadas07/modbus-frame-ledger/commit/19cf250a7c17cbfa84ef440b7e6842de39be209a) | PASSED | 0 / 0 |
| [npm-export-witness](https://github.com/nripankadas07/npm-export-witness) | [`300de90f6731`](https://github.com/nripankadas07/npm-export-witness/commit/300de90f6731ca65d1801e47c58bcfff7981ef67) | PASSED | 0 / 0 |
| [obj-island-audit](https://github.com/nripankadas07/obj-island-audit) | [`6932a0807879`](https://github.com/nripankadas07/obj-island-audit/commit/6932a0807879693cad77e5e4f31d177bbdd631d4) | PASSED | 0 / 0 |
| [oci-whiteout-plan](https://github.com/nripankadas07/oci-whiteout-plan) | [`0b0dc8442b6b`](https://github.com/nripankadas07/oci-whiteout-plan/commit/0b0dc8442b6b88531b2fc1dc5e36bdfb37519cf1) | PASSED | 0 / 0 |
| [otel-span-witness](https://github.com/nripankadas07/otel-span-witness) | [`bb995f7a934d`](https://github.com/nripankadas07/otel-span-witness/commit/bb995f7a934dcfa6f8a00398e6fd98cead249458) | PASSED | 0 / 0 |
| [pcap-flow-ledger](https://github.com/nripankadas07/pcap-flow-ledger) | [`8c8f09535532`](https://github.com/nripankadas07/pcap-flow-ledger/commit/8c8f095355323d35a5a133133748f6e82740a12c) | PASSED | 0 / 0 |
| [pdb-drain-witness](https://github.com/nripankadas07/pdb-drain-witness) | [`477f3f1dfc5b`](https://github.com/nripankadas07/pdb-drain-witness/commit/477f3f1dfc5b866ab39e286e360aa91fc0e39f30) | PASSED | 0 / 0 |
| [pg-lock-witness](https://github.com/nripankadas07/pg-lock-witness) | [`c3d5fe6e4f4c`](https://github.com/nripankadas07/pg-lock-witness/commit/c3d5fe6e4f4c835af797001c04b90b08d6b24098) | PASSED | 0 / 0 |
| [pgn-clock-ledger](https://github.com/nripankadas07/pgn-clock-ledger) | [`76fffed24a04`](https://github.com/nripankadas07/pgn-clock-ledger/commit/76fffed24a0495e241770ab9cee8110b699c416e) | PASSED | 0 / 0 |
| [prom-label-budget](https://github.com/nripankadas07/prom-label-budget) | [`9ffc56b0b793`](https://github.com/nripankadas07/prom-label-budget/commit/9ffc56b0b79332be980ab68330137d4143b86bc0) | PASSED | 0 / 0 |
| [s3-expiry-witness](https://github.com/nripankadas07/s3-expiry-witness) | [`7f1c4f85cbe1`](https://github.com/nripankadas07/s3-expiry-witness/commit/7f1c4f85cbe1612e9966fc0c475f6acf512c26c6) | PASSED | 0 / 0 |
| [san-coverage-plan](https://github.com/nripankadas07/san-coverage-plan) | [`81059d79eb63`](https://github.com/nripankadas07/san-coverage-plan/commit/81059d79eb63df95d3ce7f03088ab18d3e084bb6) | PASSED | 0 / 0 |
| [spdx-expression-paths](https://github.com/nripankadas07/spdx-expression-paths) | [`35d2b8607e2d`](https://github.com/nripankadas07/spdx-expression-paths/commit/35d2b8607e2db1314d308dfaf2377df797fa11a1) | PASSED | 0 / 0 |
| [sqlite-fixture-closure](https://github.com/nripankadas07/sqlite-fixture-closure) | [`c01bdff6da64`](https://github.com/nripankadas07/sqlite-fixture-closure/commit/c01bdff6da64db6e5083a450849887eb23cb6c68) | PASSED | 0 / 0 |
| [ssh-option-witness](https://github.com/nripankadas07/ssh-option-witness) | [`1609713c44ac`](https://github.com/nripankadas07/ssh-option-witness/commit/1609713c44acfd8844dd21bcba204545864c4213) | PASSED | 0 / 0 |
| [systemd-order-audit](https://github.com/nripankadas07/systemd-order-audit) | [`1ed90152f8cb`](https://github.com/nripankadas07/systemd-order-audit/commit/1ed90152f8cb3abf0876493b6d1623d7474c0401) | PASSED | 0 / 0 |
| [tar-link-boundary](https://github.com/nripankadas07/tar-link-boundary) | [`51463a9cbb34`](https://github.com/nripankadas07/tar-link-boundary/commit/51463a9cbb348fb78e55411b938e1de6b9c8ad59) | PASSED | 0 / 0 |
| [tf-move-witness](https://github.com/nripankadas07/tf-move-witness) | [`cf3340a60e33`](https://github.com/nripankadas07/tf-move-witness/commit/cf3340a60e33d8bf48b55a23e18679250d53d9cb) | PASSED | 0 / 0 |
| [vcd-state-ledger](https://github.com/nripankadas07/vcd-state-ledger) | [`17ee488c96d3`](https://github.com/nripankadas07/vcd-state-ledger/commit/17ee488c96d35063e6f042c2d61ec6ebfbd8b4e4) | PASSED | 0 / 0 |

## Feedback and adoption evidence

Fresh open-report inventories found no reproducible user report requiring a repair. Public stars/forks/subscriber counts and observation timestamps are a first-observed baseline in [metrics](WEEKLY_METRICS_2026-10-18.json), not verified users, retention, downloads or business impact. No change or growth claim is made without a comparable dated prior baseline. Private traffic/download analytics were unavailable through the supported connector used here. Zero stars is not evidence of no value.

## Maintenance burden and next briefs

No confirmed current failure was reproduced in these35 fresh installs. Their small offline packages share limited build infrastructure but have distinct format/domain contracts. Retain exact input caps, clean installed-command checks and explicit unsupported cases; avoid needless runtime services/dependencies. Today’s briefs apply these findings with format-specific malformed-input coverage and clear evidence limits. Do not infer support burden from silence: private usage and closed-channel feedback were not measured.

[Detailed validation receipts](WEEKLY_VALIDATION_2026-10-18.json) retain commands/results and exact public heads. Windows/macOS, every optional configuration, production datasets and broad deployment reliability remain unassessed. Three linked flagship browser demos responded today; this is a page check, not complete deployment certification.
