# Runner Reference

The benchmark runner is owned by the main `rv198-star/Mindthus` repository or
its release package. This repository must not fork, edit, or vendor runner code.

## Expected External Runner

- Main repository path:
  `scripts/run-judgment-benchmark-cli.py`
- Public main inspected:
  `a98e2929b7c67a716faddb56a46e039f6b3e0b09`
- Public tag inspected: `v1.4.4-diag`
- SHA-256 from
  `shasum -a 256 scripts/run-judgment-benchmark-cli.py`:
  `973b9ae9cbb985289c8e2447531b055b80ee8621236bdc0f2bb152a31b1057a0`

## Run-History Note

The V5 targeted-validation diagnostic was produced before the register-hints
runner landed and records runner SHA-256
`80c8b57ffe89648a14b590919e340c8e68357ed865564faf886755072e29bf02`.

The V5 register-hints diagnostic and current public main use the runner SHA-256
above, with expected prefix `973b9ae9cbb9`.

## Use Rule

When the external runner is available, run it from the main repository or from
the release package built by `build-release-pack.py`. Do not copy it into this
repository.
