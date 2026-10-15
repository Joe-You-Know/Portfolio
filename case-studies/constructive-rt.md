# ConstructiveRT: diagnose before changing a system

**Focus:** Windows diagnostics, explainable classification, and transfer measurement.

Large user-profile directories and slow downloads can invite guesses that lead to unsafe cleanup or the wrong performance fix. ConstructiveRT is a local Python toolkit organized around observing a boundary, writing a report, and keeping consequential changes separate from the audit.

The AppData audit scans Local and Roaming folders, classifies top-level boundaries, and writes JSON, text, and CSV reports. It flags large, stale folders for manual review while marking sensitive state such as wallets, mail, browser profiles, and application configuration as keep/report-only. The audit itself does not delete or quarantine files. A separate transfer profiler observes stages such as first file appearance, file growth, completion, hashing, local read throughput, and network timing.

## Evidence and limits

The source tree contains documentation and smoke/planner tests. For this case study, I inspected the implementation documentation; I did not rerun the test suite or independently benchmark the tools. The profiler observes the local machine and reported network signals. It does not intercept HTTPS or establish the root cause of every slowdown from a single run.

## Skills demonstrated

- Python tooling for Windows filesystem and network observations
- Report-first workflows that protect sensitive user state
- Turning a vague performance complaint into separate measurable stages

ConstructiveRT is currently a local project. A curated public code release would require a separate source and data review.

[Back to portfolio](../README.md)
