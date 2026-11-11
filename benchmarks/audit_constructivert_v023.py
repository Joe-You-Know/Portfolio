#!/usr/bin/env python3
"""Audit the PUBLIC ConstructiveRT v0.23 aggregate record.

This script validates a saved JSON summary and calculates relative medians.
It does NOT rerun downloads, verify external network events, or certify the
private native implementation. Python 3.9+, standard library only.
"""

import argparse
import hashlib
import json
from pathlib import Path


DEFAULT_RECORD = Path(__file__).with_name("constructivert_v023_windows.json")


def audit(record):
    if record.get("schema") != "constructivert-v023-windows-summary-v1":
        raise ValueError("Unexpected record schema")

    fixture = record["fixture"]
    digest = fixture["sha256"]
    if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
        raise ValueError("Fixture digest must be lowercase SHA-256 hex")
    if not isinstance(fixture["bytes"], int) or fixture["bytes"] <= 0:
        raise ValueError("Invalid fixture size")

    plan = record["trial_plan"]
    methods = record["methods"]
    expected_ids = {"curl", "native-full", "native-ranges"}
    if len(methods) != 3 or {x["id"] for x in methods} != expected_ids:
        raise ValueError("Expected exactly three distinct methods")
    if plan["methods"] != len(methods):
        raise ValueError("Methods count mismatch")
    if plan["trials_per_method"] * len(methods) != plan["total_trials"]:
        raise ValueError("Total-trial count mismatch")
    if plan["verified_successes"] != plan["total_trials"]:
        raise ValueError("Not every reported trial was verified")
    if plan["execution_orders"] != "all six permutations represented twice":
        raise ValueError("Unexpected ordering-control description")

    t = record["native_test_record"]
    for tag in ("windows_ctest", "linux_ctest"):
        if t[tag + "_passed"] != t[tag + "_total"] or t[tag + "_total"] <= 0:
            raise ValueError("Incomplete reported CTest pass count: " + tag)
    if t["source_manifest_sha256_passed"] != t["source_manifest_entries"]:
        raise ValueError("Source manifest check count mismatch")

    medians = {}
    for method in methods:
        value = method["median_elapsed_ms"]
        if type(value) not in (float, int) or value <= 0:
            raise ValueError("Invalid median for " + method["id"])
        medians[method["id"]] = float(value)

    baseline = medians["curl"]
    comparisons = {
        method_id: 100.0 * (median / baseline - 1.0)
        for method_id, median in medians.items()
        if method_id != "curl"
    }
    return medians, comparisons


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, default=DEFAULT_RECORD)
    args = parser.parse_args()

    record_bytes = args.record.read_bytes()
    record = json.loads(record_bytes)
    medians, comparisons = audit(record)
    print("Record: " + str(args.record))
    print("Summary SHA-256: " + hashlib.sha256(record_bytes).hexdigest())
    print("Reported verified trials: %s/%s" % (
        record["trial_plan"]["verified_successes"], record["trial_plan"]["total_trials"]
    ))
    for key in ("curl", "native-full", "native-ranges"):
        print("%s: %.3f ms median" % (key, medians[key]))
    for key in ("native-full", "native-ranges"):
        print("%s relative to curl: %+.2f%%" % (key, comparisons[key]))
    print("Scope: aggregate consistency only; no downloads or raw-trial audit.")


if __name__ == "__main__":
    main()
