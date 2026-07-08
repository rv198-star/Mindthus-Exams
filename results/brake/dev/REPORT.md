# Brake Dev Semantic-Triage Run Report

Status: dev n=3 green. Diagnostic/training only; not Mindthus certification.

## Scope

- Source fixture: `fixtures/brake/dev_cases.jsonl`
- Mechanical runner remap: `results/brake/dev/runner-remap.semantic-triage.jsonl`
- Runner mode: `--v5-semantic-triage-hints`, `--v5-register-hints=false`
- Model: `gpt-5.5`
- Judge model: `gpt-5.5`
- Runner commit: `a6fbbe9e9ffd416c56b08941bd6ef7abb2fd985c`
- Runner SHA-256: `1ca5c48f4b4ad4bb5fc314d07c2fa66ad64b13356392c986ff5584196c9d4ed8`

## Patch Summary

| Change | Means Type | Purpose |
| --- | --- | --- |
| Anti-Spiral same-class override/branch semantic features | mechanical_runtime | Let external brake cases match disease-level features without case IDs |
| D2 regex branch feature-level action probe | mechanical_runtime | Require validator/parser replacement or bounded emergency debt |
| N1 mixed-change stay-asleep probe | mechanical_runtime | Treat unrelated prior edits as ordinary feature work and avoid runtime false wake |

No method-body wording clause was added for this run.

## Repeat Summary

| Repeat | Positive Mean | Overall Mean | Score-2 Count | N1 Final False Wake Rate | N1 Runtime False Wake Rate | Owner Verdicts |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 2.0 | 2.0 | 3/3 | 0.0 | 0.0 | EXB-D1:no_load, EXB-D2:expected_owner_loaded, EXB-N1:direct_stay_asleep |
| 2 | 2.0 | 2.0 | 3/3 | 0.0 | 0.0 | EXB-D1:expected_owner_loaded, EXB-D2:expected_owner_loaded, EXB-N1:direct_stay_asleep |
| 3 | 2.0 | 2.0 | 3/3 | 0.0 | 0.0 | EXB-D1:expected_owner_loaded, EXB-D2:expected_owner_loaded, EXB-N1:direct_stay_asleep |

## Case Summary

| Case | Scores | Owner Verdicts | Hint Applied | Loaded Owner | Runtime False Wake |
| --- | --- | --- | --- | --- | --- |
| EXB-D1 | 2 / 2 / 2 | no_load / expected_owner_loaded / expected_owner_loaded | yes / yes / yes | [] / ['3l5s'] / ['3l5s'] | False / False / False |
| EXB-D2 | 2 / 2 / 2 | expected_owner_loaded / expected_owner_loaded / expected_owner_loaded | yes / yes / yes | ['3l5s'] / ['3l5s'] / ['3l5s'] | False / False / False |
| EXB-N1 | 2 / 2 / 2 | direct_stay_asleep / direct_stay_asleep / direct_stay_asleep | yes / yes / yes | [] / [] / [] | False / False / False |

## Gate Result

- D1/D2 semantic hint applied in all 3 repeats.
- EXB-D1 scores: 2 / 2 / 2.
- EXB-D2 scores: 2 / 2 / 2.
- EXB-N1 scores: 2 / 2 / 2.
- EXB-N1 final-answer false wake count: 0/3.
- EXB-N1 runtime-event false wake count: 0/3.
- Generator contamination: 0.
- Judge contamination: 0.

Prepatch diagnostic runs are retained under `semantic-triage-prepatch-*` for audit traceability; final candidate runs are `semantic-triage-repeat-1` through `semantic-triage-repeat-3`.
