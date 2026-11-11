# Research: CIM / PCL and exact computational experiments

This section separates the underlying mathematical ideas, bounded executable tests and unresolved research problems.

| Research thread | Public material | Verification boundary |
| --- | --- | --- |
| Primitive Constructive Logic (PCL) | [Foundations manuscript v1.4](../papers/primitive-constructive-logic-v1.4.pdf) | Author's formal arguments; not independent peer review |
| Primitive Measure Theorem | [Selected manuscript](../papers/primitive-measure-theorem-2026.pdf) | Conditional construction argument, not empirical proof of all physical claims |
| Exact algebra / simplex-ledger | [Case study](../case-studies/exact-algebra.md) | 56 tests passed for finite/symbolic cases; unresolved wider case remains |
| Generator-aware prime retention | [v12 research capsule](cim-generator-audit-v12.md) | 48-bit **generator-state** counting checked; no generic RSA/DLP break |
| Other CIM/DLO investigations | [Project scope notes](cim-generator-audit-v12.md) | Private active source; individual claimed certificates need independent audit |
| Numerical optics | [Double-slit simulator case study](../case-studies/double-slit-simulation.md) | Numerical prototype and parameter sweep, not physical validation |

**Source access:** [CIM](https://github.com/Joe-You-Know/CIM) is currently a **private** GitHub repository. External visitors should use the public papers, case studies and [public benchmark](../benchmarks/README.md); no private source accessibility is implied by this index.

## Research reporting rules

Keep representation separate from mechanism, hypotheses separate from measurements, and saved calculations separate from independent validation. For cryptographic topics, explicitly state factor sizes, public information supplied to the algorithm, generator/seed assumptions, comparison baselines, runtime and unresolved complexity. Do not infer source identity from hidden test controls.

[Back to portfolio](../README.md)
