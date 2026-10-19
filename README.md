# Himanshu Python World

Himanshu Python World is a deterministic catalog of 204 Python reference
solutions selected from LeetCode problems 101–300 and 600–657. The randomized
catalog order is recorded in `manifest.tsv`. The first 137 entries use Python's
`random.Random("HimanshuGarg701-python-world-2024-2026")`; the 67-entry additive
batch uses `random.Random("HimanshuGarg701-python-world-batch2-2024-2026")`.

> **Research disclosure:** Commit dates from January 1, 2024 through October
> 21, 2026 are synthetic/backfilled research history. They are generated for a
> research dataset and do not claim that this repository or its work existed on
> those dates.

> **Second additive batch disclosure:** The 67 solutions added in the second
> batch also use synthetic/backfilled commit dates from January 1, 2024 through
> October 21, 2026. These additive dates are research-dataset metadata only and
> do not represent the historical creation dates of the solutions.

Some LeetCode database and shell exercises are represented by equivalent Python
functions over rows or text so that every selected module remains importable.

## Layout

- `python_world/` contains the selected solution modules and shared structures.
- `manifest.tsv` lists the problem number, module path, and inferred title in
  randomized commit order.
- `tests/test_catalog.py` checks the manifest and imports every selected module.

## Verify

```sh
./verify.sh
```
