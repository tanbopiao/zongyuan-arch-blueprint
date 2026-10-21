#!/usr/bin/env python3
"""Validate public examples and basic schema contracts."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    sample = ROOT / "examples" / "api-router-call-check.json"
    data = json.loads(sample.read_text(encoding="utf-8"))
    required = {
        "status", "choose", "tier", "capability", "smoke_code",
        "quota_hint", "why", "fallbacks", "local_reachable", "local_fused", "updated_at",
    }
    missing = required - set(data)
    if missing:
        raise SystemExit(f"missing required fields: {sorted(missing)}")
    if data["status"] not in {"OK", "DEGRADED", "LOCAL_FALLBACK", "NO_ROUTE"}:
        raise SystemExit("status must be one of OK, DEGRADED, LOCAL_FALLBACK, NO_ROUTE")
    if not isinstance(data["fallbacks"], list) or not data["fallbacks"]:
        raise SystemExit("fallbacks must be a non-empty list")
    print("Example validation passed: examples/api-router-call-check.json")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
