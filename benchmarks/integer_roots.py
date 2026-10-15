"""Reproducible integer-root comparison; no external packages required.

This is a new reference demonstration. It does not reproduce the historical
root-arithmetic benchmark JSON files in the research workspace.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import random
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


def binary_root(value: int, degree: int) -> int:
    """Return the floor of the nonnegative integer degree-root by bisection."""
    if value < 0 or degree < 2:
        raise ValueError("value must be nonnegative and degree at least two")
    if value < 2:
        return value
    low = 0
    high = (1 << ((value.bit_length() + degree - 1) // degree)) + 1
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**degree <= value:
            low = middle
        else:
            high = middle
    return low


def radix_block_root(value: int, degree: int, block_bits: int) -> int:
    """Lift one root digit at a time in base 2**block_bits."""
    if value < 0 or degree < 2 or block_bits < 1:
        raise ValueError("value must be nonnegative; degree and block_bits positive")
    if value < 2:
        return value
    root_base = 1 << block_bits
    value_base = root_base**degree
    chunks = []
    remaining = value
    while remaining:
        remaining, chunk = divmod(remaining, value_base)
        chunks.append(chunk)
    prefix = 0
    root = 0
    for chunk in reversed(chunks):
        prefix = prefix * value_base + chunk
        root_prefix = root * root_base
        low_digit = 0
        high_digit = root_base - 1
        while low_digit < high_digit:
            middle_digit = (low_digit + high_digit + 1) // 2
            if (root_prefix + middle_digit) ** degree <= prefix:
                low_digit = middle_digit
            else:
                high_digit = middle_digit - 1
        root = root_prefix + low_digit
    return root


def check_root(value: int, degree: int, root: int) -> None:
    if not (root**degree <= value < (root + 1) ** degree):
        raise AssertionError("integer-root boundary check failed")


def self_test() -> None:
    rng = random.Random(913)
    values = list(range(151)) + [rng.getrandbits(bits) for bits in (64, 128, 256, 1023)]
    for degree in (2, 3, 5):
        for value in values:
            reference = math.isqrt(value) if degree == 2 else binary_root(value, degree)
            check_root(value, degree, reference)
            for block_bits in (2, 4, 8, 16, 32):
                result = radix_block_root(value, degree, block_bits)
                check_root(value, degree, result)
                if result != reference:
                    raise AssertionError("radix-block and reference roots differ")


def median_ns(function, repeats: int) -> int:
    samples = []
    for _ in range(repeats):
        started = time.perf_counter_ns()
        function()
        samples.append(time.perf_counter_ns() - started)
    return int(statistics.median(samples))


def benchmark(bits: tuple[int, ...], block_bits: tuple[int, ...], repeats: int) -> dict:
    if repeats < 1 or any(x < 2 for x in bits) or any(x < 1 for x in block_bits):
        raise ValueError("bits, block_bits, and repeats must be positive")
    rng = random.Random(913)
    cases = []
    for bit_count in bits:
        value = rng.getrandbits(bit_count) | (1 << (bit_count - 1))
        fixture_hash = hashlib.sha256(value.to_bytes((bit_count + 7) // 8, "big")).hexdigest()
        for degree in (2, 3):
            reference_function = (lambda: math.isqrt(value)) if degree == 2 else (lambda: binary_root(value, degree))
            reference = reference_function()
            check_root(value, degree, reference)
            reference_ns = median_ns(reference_function, repeats)
            variants = []
            for width in block_bits:
                candidate_function = lambda width=width: radix_block_root(value, degree, width)
                candidate = candidate_function()
                check_root(value, degree, candidate)
                if candidate != reference:
                    raise AssertionError("candidate differs from reference")
                variants.append({"block_bits": width, "median_ns": median_ns(candidate_function, repeats)})
            cases.append({
                "operand_bits": bit_count,
                "degree": degree,
                "fixture_sha256": fixture_hash,
                "reference": "math.isqrt" if degree == 2 else "binary_search",
                "reference_median_ns": reference_ns,
                "radix_block_variants": variants,
            })
    return {
        "description": "Fresh, self-contained integer-root comparison; not a reproduction of earlier saved benchmarks",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "seed": 913,
        "repeats_per_measurement": repeats,
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--bits", type=int, nargs="+", default=[1023, 4095, 8192])
    parser.add_argument("--block-bits", type=int, nargs="+", default=[8, 16, 32])
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    self_test()
    if args.self_test:
        print("SELF_TEST_OK")
        return
    result = benchmark(tuple(args.bits), tuple(args.block_bits), args.repeats)
    content = json.dumps(result, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
