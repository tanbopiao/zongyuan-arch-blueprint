#!/usr/bin/env python3
"""Scan the repository for public-safety violations.

Public repos must not contain private credentials, keys, personal hostnames,
or private endpoint details. This tool uses conservative pattern matching
so it can run inside the public repository itself.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Patterns that should never appear in public content.
LEAK_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("github_pat", re.compile(r"github_pat_[A-Za-z0-9_-]{20,}")),
    ("gitee_token", re.compile(r"(?i)gitee[_-]?token[^\n]{0,40}")),
    ("generic_bearer", re.compile(r"(?i)authorization\s*:\s*Bearer\s+[A-Za-z0-9._-]{20,}")),
    ("private_key_block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("ssh_public_key", re.compile(r"ssh-ed25519\s+[A-Za-z0-9+/=]{40,}")),
    ("aws_access_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("generic_api_key", re.compile(r"(?i)(api[_-]?key|secret[_-]?token|access[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9._-]{16,}")),
    ("personal_endpoint", re.compile(r"(?i)https?://[a-z0-9.-]+(?:\.internal|\.lan|\.corp|\.private)")),
    ("ipv4_private", re.compile(r"\b(10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b")),
]

SKIP_DIRS = {".git", "node_modules", "__pycache__", "dist", "build"}
SELF_SCAN_RELPATH = "tools/check_public_safety.py"
SELF_VERIFY_RELPATH = "tools/verify_public_repo.py"


def should_skip(path: Path) -> bool:
    if path.name in SKIP_DIRS:
        return True
    rel = path.relative_to(ROOT).as_posix()
    if rel in {SELF_SCAN_RELPATH, SELF_VERIFY_RELPATH, "tools/prepush.sh"}:
        return True
    return False


def scan(path: Path) -> list[tuple[str, str, str]]:
    """Return (file, line, pattern_name) for each leak found."""
    findings: list[tuple[str, str, str]] = []
    if path.is_dir():
        for child in path.iterdir():
            if should_skip(child):
                continue
            findings.extend(scan(child))
        return findings
    if should_skip(path):
        return findings
    if path.suffix not in {".md", ".json", ".yaml", ".yml", ".txt", ".ts", ".js", ".py", ".sh"}:
        return findings
    rel = path.relative_to(ROOT).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return findings
    for line_no, line in enumerate(text.splitlines(), start=1):
        for pattern_name, pattern in LEAK_PATTERNS:
            if pattern.search(line):
                findings.append((rel, f"L{line_no}: {line.strip()[:80]}", pattern_name))
    return findings


def main() -> int:
    findings = scan(ROOT)
    if findings:
        print("Public safety scan failed. Leaks detected:")
        for rel, line, pattern in findings:
            print(f"  {rel} :: {line} :: {pattern}")
        return 1
    print("Public safety scan passed: no credential or private endpoint patterns found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
