#!/usr/bin/env python3

import os
import subprocess
import sys
import tempfile
from pathlib import Path

# Run from the root of your HW3 project directory.
PARSER = Path("./src/legacy_log_parser_fixed")
EXPLOIT_PAYLOAD = Path("./inbox/payload.bin")
MARKER = Path("./markers/ret2win.txt")


def marker_state():
    """Capture marker metadata so the test can detect changes."""
    try:
        stat = MARKER.stat()
        return (stat.st_ino, stat.st_size, stat.st_mtime_ns)
    except FileNotFoundError:
        return None


def run_parser(input_path):
    """Run the parser and capture its output."""
    return subprocess.run(
        [str(PARSER), str(input_path)],
        capture_output=True,
        text=True,
        timeout=5
    )


def check_result(name, result, should_accept, expected_message=None):
    """Print PASS or FAIL based on the parser's response."""
    accepted = result.stderr == "" and result.returncode == 0

    if should_accept:
        passed = accepted
    else:
        passed = (
            not accepted
            and (
                expected_message is None
                or expected_message in result.stderr
            )
        )

    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")

    if not passed:
        print(f"       Exit code: {result.returncode}")
        print(f"       stdout: {result.stdout.strip()!r}")
        print(f"       stderr: {result.stderr.strip()!r}")
    return passed


def main():
    if not PARSER.exists():
        print(f"Parser not found: {PARSER}")
        print("Compile the fixed parser first.")
        return 1

    failures = 0

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)

        # Test 1: Short input should be accepted.
        short_file = temp / "short.bin"
        short_file.write_bytes(b"shortlog")
        result = run_parser(short_file)
        check_result("Short input (8 bytes)", result, True)

        # Test 2: Exactly 127 bytes should be accepted.
        max_file = temp / "max.bin"
        max_file.write_bytes(b"A" * 127)
        result = run_parser(max_file)
        check_result("Maximum input (127 bytes)", result, True)

        # Test 3: 128 bytes should be rejected.
        oversized_file = temp / "oversized.bin"
        oversized_file.write_bytes(b"A" * 128)
        result = run_parser(oversized_file)
        check_result(
            "One byte over maximum (128 bytes)",
            result,
            False,
            "input too large"
        )

        # Test 4: Missing file should be handled.
        missing_file = temp / "does_not_exist.bin"
        result = run_parser(missing_file)
        check_result(
            "Missing input file",
            result,
            False,
            "parse_log: fopen"
        )

    # Test 5: Original Task 1 exploit payload should be rejected.
    if EXPLOIT_PAYLOAD.exists():
        before = marker_state()
        result = run_parser(EXPLOIT_PAYLOAD)
        after = marker_state()

        passed = (
            "input too large" in result.stderr
            and before == after
        )

        print(
            f"[{'PASS' if passed else 'FAIL'}] "
            "Original Task 1 exploit payload"
        )

        if not passed:
            print(f"       Exit code: {result.returncode}")
            print(f"       stderr: {result.stderr.strip()!r}")
            print("       Marker before:", before)
            print("       Marker after: ", after)

        if not passed:
            failures += 1
    else:
        print("[SKIP] Original Task 1 exploit payload not found")
        print(f"       Expected: {EXPLOIT_PAYLOAD}")

    print("\nTesting complete.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())