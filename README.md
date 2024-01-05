# Himanshu Python World

Himanshu Python World is a deterministic catalog of 137 Python reference
solutions selected from LeetCode problems 101–200 and 230–280. The randomized
catalog order is recorded in `manifest.tsv` and can be reproduced with Python's
`random.Random("HimanshuGarg701-python-world-2024-2026")`.

> **Research disclosure:** Commit dates from January 1, 2024 through October
> 21, 2026 are synthetic/backfilled research history. They are generated for a
> research dataset and do not claim that this repository or its work existed on
> those dates.

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
