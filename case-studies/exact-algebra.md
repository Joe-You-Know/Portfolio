# Exact algebra research software

**Focus:** symbolic computation, reproducible checks, and bounded mathematical claims.

Research code is most useful when a reader can see the identities being checked, the cases covered, and the exceptions that remain. I developed a Python/SymPy package for an exact simplex-ledger investigation, with symbolic identities, a finite signature census, certificate output, and an automated test suite.

The package records a degree-36 carrier classification with 99,133 reported multiplicity signatures. Its summary reports 99,124 full-carrier cases at the third shell and retains exceptional branches. The complete (72,108) case remains unresolved; the finite census does not settle it.

## Evidence and limits

An isolated copy of version 1.9 was checked on September 10, 2026: **56 tests passed with no failures or errors**. The run included symbolic reconstruction, branch coverage, the signature census, and third-shell identities. A source-hash check found the 105 original package files unchanged. Those checks support the implementation and the tested finite cases. They do not constitute an independent proof of every wider mathematical claim.

## Skills demonstrated

- Python and SymPy for exact symbolic work
- Automated verification and reproducible execution records
- Clear treatment of unresolved cases

The full research package and execution record are local working artifacts. This public case study is a bounded description of that work; source and detailed certificates can be prepared for review separately.

[Back to portfolio](../README.md)
