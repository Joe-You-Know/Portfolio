# CIM: generator-aware ordered-cause counting — v12 audit capsule

**Experimental checkpoint:** November 9, 2026 (local Linux/libisl; private experimental branch).

## Research question

Can an exact, source-attributed reconstruction preserve useful information about rejected candidate histories, rather than re-enumerating every compatible terminal state? This experiment works with a **known toy affine generator policy**, not a general-purpose factorization oracle.

## Construction and controlled comparison

The experiment uses the toy map

`T(x) = 1664525*x + 1013904223 (mod 2^w)`

and tracks ordered rejected predecessor causes. For this odd multiplier, a half-modulus shift of a generator state complements a four-step flag configuration while preserving the corresponding forced-top/odd candidate words and their first-divisor cause. For the tested configurations, eight representative flags can be counted and doubled to cover sixteen.

The v12 local research note reports a six-dimensional ISL lattice-point counter cross-checked against small exhaustive baselines or an earlier explicit scanner.

| Candidate bits | Generator-state bits | Ordered cause | Exact counted states | Reference |
| ---: | ---: | --- | ---: | --- |
| 8 | 20 | 3 then 5 | 10 | Exhaustive brute force |
| 8 | 24 | 3 then 5 | 158 | v11 |
| 12 | 32 | 5 then 3 | 200 | v11 |
| 12 | 48 | 3 then 5 | **11,910,626** | v11 explicit scan |
| 12 | 48 | 5 then 3 | **11,911,062** | v11 explicit scan |

At 48-bit generator-state width, the v12 symbolic count matched the explicit reference counts without scanning its 268,515,928 product-compatible terminal states in the counting stage. These are **generator-state widths**, not RSA modulus or factor lengths. The 12-bit candidate-prime regime, known generator policy, and ordinary `N mod p` candidate check limit the conclusion.

## Failed boundary and what it means

A 64-bit generator-state single-cause/flag computation **timed out after 90 seconds**. It did not establish an exact total at that width, and the experiment does not establish public-`N`-only inversion or cryptographic-size speedup. The documented 64-bit count remained bounded rather than exact; the separate Monte Carlo estimate was only a statistical diagnostic.

## Reproduction status

The private research branch retains Python/ISL experimental source, result JSON, and an offline execution note. It is **not published as runnable source in this public portfolio**. The public [integer-root benchmark](../benchmarks/README.md) is an unrelated independently runnable exact-arithmetic example, not a reproduction of these prime-retention results.

Next: derive an exact scalable complete joint-prime count, track memory and complexity, and compare against appropriately informed conventional baselines and negative controls.

[Research index](README.md) · [Portfolio home](../README.md)
