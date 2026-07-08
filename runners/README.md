# Runner Reference

The benchmark runner is owned by the main `rv198-star/Mindthus` repository or
its release package. This repository must not fork, edit, or vendor runner code.

## Expected External Runner

- Main repository path named in the build spec:
  `scripts/run-judgment-benchmark-cli.py`
- Required SHA-256 prefix from the build spec: `4e11d650`
- Full SHA-256: not supplied in the static build-spec material.

## Inspection Note

At this static delivery, public main HEAD
`d0746545cccf7b91a68fb989adcfaad9a128ff89` does not contain
`scripts/run-judgment-benchmark-cli.py`. Until the runner is published or the
release artifact is provided, this repository only pins the expected reference
and keeps fixtures remappable.

## Use Rule

When the external runner is available, run it from the main repository or from
the release package built by `build-release-pack.py`. Do not copy it into this
repository.
