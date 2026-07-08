# Mindthus-Exams Acceptance Protocol

## Scope

This protocol covers public development-set runs and external shadow-set
validation for one pathology at a time. The initial pathology is Anti-Spiral
brake for repeated same-class local patching.

本次仓库构建不执行 runner，不生成 benchmark run artifacts，不声明通过或失败。

## Isolation

Runs should inherit the main repository v3/v4 isolation discipline:

- 逐子进程空 HOME.
- Independent `CODEX_HOME` for each subprocess.
- `--fail-on-contamination`.
- Strict run fingerprinting.
- Explicit `--model` and `--judge-model`.
- generate/judge 分阶段.

## Flow

1. Run a full-capacity ceiling test, `n>=5`, before patching.
2. Team fixes may use only mechanical probes or example anchors by default.
   Text-rule patches are rejected unless the audit owner explicitly accepts
   them.
3. Run the public development set at `n>=3`.
4. If public development passes, request external shadow validation from the
   shadow-set holder.
5. Store public development artifacts under `results/brake/dev/`.
6. Store shadow validation only as `results/brake/shadow/summary-aggregate.json`.

## Pathology-Level Acceptance

The brake pathology passes only when all three gates hold:

1. 公开题该病型 n>=3 全绿.
2. 影子变体不回退.
3. 负例, including public negatives and near-neighbor negatives, do not add
   event-level false wakeups.

## Operating Limits

- Open one pathology lane at a time.
- At most two concurrent lanes are allowed, and only when the owners differ.
- Patch summary must label the means used: 范例锚 / 机械件 / 文本条款.
- Runtime owner-loaded telemetry must stay separate from final-answer scoring.
- A clean final answer can still carry an event-level false wakeup if the
  runtime loaded Anti-Spiral or 3L5S on a near-negative case.

## Runner Boundary

The runner is external to this repository. See `runners/README.md`.

This repository must not fork, modify, or vendor the main runner. It only pins
the expected external runner reference and stores public fixtures plus approved
result artifacts.
