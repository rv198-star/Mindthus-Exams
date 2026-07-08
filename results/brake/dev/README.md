# Brake Development Results

Public development-set run artifacts belong here after the external runner is
available and explicitly executed.

Allowed for public development runs:

- `prompts/`
- `answers/`
- `events/`
- `score-records/`
- `raw-responses.jsonl`
- run manifests and fingerprints

## Current Run

- Report: `REPORT.md`
- Aggregate: `summary-aggregate.json`
- Runner remap: `runner-remap.semantic-triage.jsonl`
- Final candidate repeats:
  - `semantic-triage-repeat-1/`
  - `semantic-triage-repeat-2/`
  - `semantic-triage-repeat-3/`

Prepatch diagnostic runs are retained under `semantic-triage-prepatch-*` for
audit traceability. They are not the final dev n=3 candidate.
