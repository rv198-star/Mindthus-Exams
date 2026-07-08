# Mindthus-Exams

Public training and acceptance rig for Mindthus pathology-specific evaluation.

This repository currently hosts the first brake pathology development set:
Anti-Spiral brake, owned by Anti-Spiral inside 3L5S. The target failure pattern
is repeated same-class local patching: after three similar local fixes, the next
same-class patch request should trigger a brake instead of another unqualified
patch.

The shadow set is intentionally outside this repository. Shadow validation only
returns aggregate results after the external holder runs it.

## Current Delivery Boundary

This repository contains the static brake rig plus the first public brake-dev
diagnostic run artifacts under `results/brake/dev/`. The public fixture,
protocol, runner pointer, rubric pointer, verdict contract, and validation tests
remain part of the delivery.

本仓库一切结果均为诊断/训练性质，不构成 Mindthus 认证。

The current public main reference for the brake-dev run is
`a6fbbe9e9ffd416c56b08941bd6ef7abb2fd985c`, a post-`v1.4.4-diag` diagnostic
commit. The benchmark runner exists at
`scripts/run-judgment-benchmark-cli.py`; this repository records its SHA in
`runners/README.md` but still does not vendor runner code.

The fixture schema in `fixtures/brake/dev_cases.jsonl` is a public brake-dev
schema. Keep the case IDs stable and remap mechanically if the external runner
requires a narrower fixture shape.

## Upstream Audit References

- V5 targeted validation:
  `docs/benchmarks/runs/2026-07-08-v5-targeted-validation/REPORT.md`
- V5 targeted validation base commit:
  `b36830626df5d61b9ffe4ec8d2a04f695e61e58c`
- V5 register-hints diagnostic:
  `docs/benchmarks/runs/2026-07-08-v5-register-hints-diagnostic/REPORT.md`
- V5 register-hints raw answer generation commit:
  `98aebe65afc6e35523062a164e70622c8c94209b`
- V5 register-hints summary reanalysis commit:
  `8b803923f986e3a38508db6b3dd0bfc543b1832f`
- V5 naturalization diagnostic:
  `docs/benchmarks/runs/2026-07-08-v5-naturalization/REPORT.md`
- Brake-dev first run:
  `results/brake/dev/REPORT.md`

## Repository Layout

```text
Mindthus-Exams/
├── README.md
├── PROTOCOL.md
├── rubric/
│   └── RUBRIC_VERSION.md
├── fixtures/
│   └── brake/
│       └── dev_cases.jsonl
├── runners/
│   └── README.md
├── results/
│   └── brake/
│       ├── dev/
│       │   └── README.md
│       └── shadow/
│           └── summary-aggregate.json
└── verdicts/
    └── brake/
        └── README.md
```

## Leakage Rules

- **R1**: 影子集题面、判分要点、题面哈希前的任何原文，禁止以任何形式进入本仓库，包括 commit history、issue、PR、wiki。
- **R2**: Shadow run 的 `prompts/`、`answers/`、`raw-responses.jsonl`、`judge-prompts/` 禁止上传，因为这些文件包含题面原文。
- **R3**: `results/*/shadow/` 只收 `summary-aggregate.json`。字段限于 case hash ID、score、owner-loaded marker、event-level false-wakeup count、run fingerprint。
- **R4**: 验收通过后，该批影子题视为半废，下一轮滚动换新，即 rotating shadow set。
- **R5**: 本仓库只消费主仓库通过 `build-release-pack.py` 构建出的插件包做热更新安装；不要主仓库写权限，也不要反向链接影子内容。

## Static Validation

Run:

```bash
python3 -m unittest discover -s tests
```

This checks repository shape, public fixture JSONL shape, and shadow leakage
guards. It does not prove model behavior or benchmark pass status.

The same command is enforced by GitHub Actions on push and pull request.
