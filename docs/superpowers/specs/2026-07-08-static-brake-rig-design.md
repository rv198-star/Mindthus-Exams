# Static Brake Rig Design

## Goal

Build the first public `Mindthus-Exams` training and acceptance rig for the
Anti-Spiral brake pathology without running the benchmark or generating model
artifacts.

## Scope

This delivery creates the repository structure, public documentation, rubric
pointer, runner pointer, public development fixtures, and static validation
tests. It does not execute the main benchmark runner, does not create dev run
artifacts beyond placeholders, and does not include any shadow-set prompt,
answer, raw response, judge prompt, or pre-hash source text.

## Architecture

The repository is a public exam harness wrapper. It contains public fixtures and
protocol metadata only, while consuming the main `rv198-star/Mindthus` release
pack and externally frozen runner/rubric references.

The development fixture uses a repository-local public JSONL schema for the
brake development set. The external runner now exists in the public main
repository, but this repository still keeps stable case identifiers, multi-turn
prompts, expected owner metadata, scoring anchors, and leakage-safe tags so the
fixture can be mechanically remapped if the runner requires a narrower case
shape.

## Files

- `README.md`: public positioning and mandatory leakage rules R1-R5.
- `PROTOCOL.md`: acceptance protocol for isolated generate/judge runs,
  triple-gate pathology acceptance, patch-summary labeling, and no-test-run
  status for this repository build.
- `rubric/RUBRIC_VERSION.md`: metadata-only pointer to the frozen rubric
  authority; no scoring details.
- `fixtures/brake/dev_cases.jsonl`: public three-case brake development set.
- `runners/README.md`: external runner reference; no forked runner code.
- `results/brake/dev/README.md`: allowed full dev artifact location.
- `results/brake/shadow/summary-aggregate.json`: leakage-safe aggregate
  placeholder only.
- `verdicts/brake/README.md`: external audit verdict record contract.
- `tests/test_static_rig.py`: static validation for structure, JSONL shape, and
  shadow leakage guardrails.

## Validation

Static validation runs with:

```bash
python3 -m unittest discover -s tests
```

This proves the committed repository structure and fixture shape. It does not
prove model behavior, runner behavior, or benchmark pass/fail status.
