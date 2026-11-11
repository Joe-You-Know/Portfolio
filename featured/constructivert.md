# ConstructiveRT — C++20 native runtime and evidence-first diagnostics

**Domains:** C++20, CMake, Windows/MSVC, HTTP(S), libcurl, OpenSSL SHA-256, SQLite, Python, measurement design.

## 1. What problem did I address?

Network downloads, user-profile storage, and local caching are often optimized based on poorly localized symptoms. A slow end-to-end operation can reflect network conditions, remote servers, TLS, storage, hashing, lock contention, or implementation behavior. I wanted observable, integrity-checked boundaries before making high-impact changes.

## 2. What did I implement?

The project has two distinct stages:

- An earlier Python toolkit that reports on Windows AppData boundaries and transfer timing without automatically deleting sensitive files.
- A **native C++20 v0.23** HTTP(S) downloader/cache with full GET and ranged transfers, SHA-256 verification, content-addressed atomic cache publication, source/ETag-aware resumable chunks, native locking, a SQLite observation ledger, and opt-in phase measurements.

Related Chrome experiments are separate from the validated native runtime.

## 3. What did I actually verify?

**Windows x64 evidence, November 10, 2026:** The submitted MSVC test log records a successful build and **3/3 passing CTest suites**. An additional clean Linux Release source build also passed **3/3 suites**. The source release's original 27-entry manifest matched **27/27** hashes and sizes.

A balanced Windows WAN comparison used an official 12,566,858-byte NumPy wheel. Twelve trials per method, rotating all six execution orders twice, completed **36/36 independently SHA-256-verified transfers**.

| Method | Observed median elapsed time |
| --- | ---: |
| curl + separate hash | **1,943.249 ms** |
| Native full GET | 1,988.228 ms |
| Native four-worker ranges | 1,999.053 ms |

**Native was not faster.** Native full GET was approximately 2.3% slower than curl and native ranges approximately 2.9% slower for these run medians. The environment and transfer-path costs must be examined before asserting general improvements.

A public [structured aggregate record](../benchmarks/constructivert_v023_windows.json) and [standard-library record checker](../benchmarks/audit_constructivert_v023.py) allow anyone to inspect the counts and recompute the median ratios. **The checker validates the recorded aggregates, not the underlying transfers**, and is not a substitute for the original native source, full raw CSV, or an independent network rerun.

For historical Python tools and test context, see the [longer case study](../case-studies/constructive-rt.md).

## 4. What remains unresolved?

- Reproduce the Windows network comparison from an independent, checked-out public source release.
- Investigate local overhead, concurrent range scheduling and interrupted-process resume correctness before performance claims.
- Test under more networks, servers, content sizes, hardware, failure modes and security conditions.
- Establish versioned release/CI policy, licensing, and sufficient reproducible raw data.

The v0.23 native source package has been curated separately but **the standalone `Joe-You-Know/ConstructiveRT` repository has not yet been created**. The associated private Good Economy Agent repository retains a validation checkpoint, not a complete public v0.23 source release.

[All featured projects](README.md) · [Portfolio home](../README.md)
