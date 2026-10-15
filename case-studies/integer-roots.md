# Exact integer-root benchmark

**Focus:** reproducible algorithms, correctness checks, and honest performance comparison.

The research workspace contains saved root-arithmetic timing records, but the original script that produced them was not located during this portfolio review. To make a runnable example available, I wrote a **new** dependency-free Python benchmark. It compares a digit-by-digit radix-block integer-root implementation with `math.isqrt` for square roots and a simple binary-search reference for cube roots. This demonstration is separate from the earlier saved measurements.

The radix-block implementation repeatedly splits the operand with exact quotient and remainder, appends one block, and finds the largest root digit whose power stays within the current prefix. Every measured result is checked against the reference and against the floor-root inequality before it is recorded.

## Run it

From the repository root on Windows:

```powershell
py -3 benchmarks\integer_roots.py --self-test
py -3 benchmarks\integer_roots.py --out benchmarks\integer_roots_results.json
```

The default run uses deterministic 1,023-, 4,095-, and 8,192-bit operands, degrees two and three, block widths 8, 16, and 32, and three timing repetitions per measurement. It saves the Python/platform version and a fixture hash. The [source](../benchmarks/integer_roots.py) and [recorded output](../benchmarks/integer_roots_results.json) are both included.

## Result and limits

The saved Windows/Python 3.12.6 run found that the radix-block method was much slower than optimized `math.isqrt` for square roots. For the 8,192-bit cube-root fixture, the 16-bit-block median was about 16.5 ms versus 34.5 ms for the simple binary-search reference. These are three-repeat, single-machine timings, not a claim of a general speedup or a comparison with optimized cube-root libraries. The self-test passed, and all measured roots passed exact boundary checks.

[Back to portfolio](../README.md)
