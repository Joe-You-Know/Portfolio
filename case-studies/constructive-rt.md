# ConstructiveRT: diagnose before changing a system

**Focus:** Windows diagnostics, explainable classification, and transfer measurement.

Large user-profile directories and slow downloads can invite guesses that lead to unsafe cleanup or the wrong performance fix. ConstructiveRT is a local Python toolkit organized around observing a boundary, writing a report, and keeping consequential changes separate from the audit.

The AppData audit scans Local and Roaming folders, classifies top-level boundaries, and writes JSON, text, and CSV reports. It flags large, stale folders for manual review while marking sensitive state such as wallets, mail, browser profiles, and application configuration as keep/report-only. The audit itself does not delete or quarantine files. A separate transfer profiler observes stages such as first file appearance, file growth, completion, hashing, local read throughput, and network timing.

## Evidence and limits

At the original October portfolio review, I inspected the Python implementation documentation without rerunning its test suite. Subsequent native v0.23 tests and benchmarks are documented below and must not be conflated with the earlier Python toolkit. The profiler observes local machine and network timing signals; it does not intercept HTTPS or establish the root cause of every slowdown from a single run.

## Native C++20 development checkpoint — November 10, 2026

A separate native C++20 downloader/cache subsystem now implements full HTTP(S) downloads, range resumption, independent SHA-256 integrity checks, atomic content-addressed cache publication, a SQLite observation ledger, and opt-in phase timing.

**Validation:** The uploaded Windows x64/MSVC test record reports all 3 CTest suites passing. I also built the curated v0.23 source with CMake on Linux on November 10 and reran those suites: **3/3 passed**. This establishes test outcomes for those source/environment conditions, not an exhaustive security review or production certification.

**Real Windows WAN benchmark:** A balanced 12-round comparison of the same 12,566,858-byte NumPy 2.1.3 wheel completed **36/36 hash-verified trials**. The recorded median elapsed times were **1,943.249 ms for curl + hash**, **1,988.228 ms for native full GET**, and **1,999.053 ms for native ranges**. All six execution orders were represented twice. The native variants did **not** outperform curl in this test; the benchmark instead identifies implementation and transfer-boundary costs worth investigating.

The full v0.23 source and verification reports are currently prepared as a standalone release snapshot; the dedicated public ConstructiveRT repository has **not yet been created**. The native C++ source should not be mistaken for code available through this public portfolio page. Earlier research branches and browser-extension experiments have separate validation scope.

## Skills demonstrated

- Python tooling for Windows filesystem and network observations
- C++20, CMake, libcurl, SQLite, OpenSSL SHA-256, and platform build validation
- Report-first workflows that protect sensitive user state
- Turning a vague performance complaint into separate measurable stages

ConstructiveRT is currently a local project. A curated public code release would require a separate source and data review.

[Back to portfolio](../README.md)
