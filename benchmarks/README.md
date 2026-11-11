# Public benchmarks and reproducible checks

These files distinguish **a runnable algorithm test**, **a saved experimental result**, and **a checker of a published summary**. None should be conflated with independent replication of private source code.

## Exact integer roots — runnable public benchmark

- [Source](integer_roots.py) · [Saved Windows result](integer_roots_results.json) · [Case study](../case-studies/integer-roots.md).
- On Windows, from the repository root:

```powershell
py -3 benchmarks\integer_roots.py --self-test
py -3 benchmarks\integer_roots.py --out benchmarks\integer_roots_results.json
```

The script compares exact digit-by-digit radix-block roots against reference implementations and checks floor-root inequalities. Running it locally replaces the saved output with your own environment's timings.

## ConstructiveRT native v0.23 — public aggregate record

- [Recorded Windows aggregates](constructivert_v023_windows.json) · [Audit script](audit_constructivert_v023.py) · [Featured study](../featured/constructivert.md).
- On Windows:

```powershell
py -3 benchmarks\audit_constructivert_v023.py
```

- On Linux/macOS:

```bash
python3 benchmarks/audit_constructivert_v023.py
```

The checker validates the published record's counts, reported method ordering, hashes and basic arithmetic; it prints the relative median overhead. **It cannot establish that recorded network transfers occurred**, independently reconstruct the original individual samples, or benchmark the private native implementation. The original Windows data were examined separately before this record was written.

## Reproducibility policy

Include the source version, environment, fixture, controlled variables, baseline, repeated runs, correctness checks and failure cases before making broad performance claims. Do not present a synthetic fixture as measured external behavior. New benchmarks should be opt-in, local and inexpensive by default; the portfolio does not contain scheduled GitHub Actions workflows.

[Back to portfolio](../README.md)
