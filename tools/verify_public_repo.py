#!/usr/bin/env python3
"""Verify that the public GitHub repository exposes the expected push mechanism."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import urllib.request
import urllib.error

REPO = "tanbopiao/zongyuan-arch-blueprint"
API_BASE = f"https://api.github.com/repos/{REPO}"
REQUIRED_FILES = [
    "docs/05-public-push-mechanism.md",
    "schemas/push-policy.md",
    "schemas/multi-data-lake-mapping.md",
    "tools/check_public_safety.py",
    "tools/validate_examples.py",
    "tools/prepush.sh",
]


def get_json(url: str) -> object:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main() -> int:
    repo = get_json(API_BASE)
    if not repo.get("visibility") == "public":
        print(f"FAIL: repo is not public (visibility={repo.get('visibility')})")
        return 1
    default_branch = repo.get("default_branch", "main")

    tree_url = f"{API_BASE}/contents/?ref={default_branch}"
    contents = get_json(tree_url)
    if not isinstance(contents, list):
        print("FAIL: could not read top-level contents listing")
        return 1

    found_names = {item.get("path") for item in contents}
    missing = [path for path in REQUIRED_FILES if path not in found_names]
    if missing:
        print(f"FAIL: missing required public files: {missing}")
        return 1

    # Confirm push gate doc mentions prepush.
    doc_url = f"{API_BASE}/contents/{REQUIRED_FILES[0]}?ref={default_branch}"
    doc = get_json(doc_url)
    doc_text = doc.get("content", "")
    if "prepush" not in doc_text:
        print("FAIL: public push doc does not reference prepush gate")
        return 1

    print(f"OK: public repo verified ({REPO}, default branch={default_branch})")
    print(f"OK: required files present: {len(REQUIRED_FILES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
