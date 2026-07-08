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

This build is a static repository delivery. It creates the public fixture,
protocol, runner pointer, rubric pointer, result directories, verdict contract,
and validation tests. It does not run the main benchmark runner and does not
generate model prompts, answers, events, score records, or judge outputs.

本仓库一切结果均为诊断/训练性质，不构成 Mindthus 认证。

The fixture schema in `fixtures/brake/dev_cases.jsonl` is provisional because
the named main runner, `scripts/run-judgment-benchmark-cli.py`, is not present
in the public `rv198-star/Mindthus` repository at inspection time. The cases are
kept stable and remappable when the formal runner schema is published.

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
