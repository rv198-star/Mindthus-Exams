# Brake Verdicts

External audit verdicts for the brake pathology belong here.

Allowed verdict statuses:

- `pass`
- `rollback`
- `false_injury`

Verdicts may include pathology-level attribution, public case IDs, shadow case
hash IDs, aggregate score movement, owner-loaded markers, event-level false
wakeup counts, run fingerprints, and patch-summary means labels.

Verdicts must not include shadow prompts, shadow answers, raw responses, judge
prompts, judging details, or any pre-hash shadow source text.
