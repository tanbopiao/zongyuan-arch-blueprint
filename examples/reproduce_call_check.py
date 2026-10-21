#!/usr/bin/env python3
"""Reproduce the sanitized call-check reporting rule.

This example does not call any external API. It reads the checked-in
sanitized state file and prints the public reporting message.
"""

import json
from pathlib import Path


def main() -> None:
    state_path = Path(__file__).with_name("api-router-call-check.json")
    state = json.loads(state_path.read_text(encoding="utf-8"))

    status = state["status"]
    main_route = state.get("choose", "unknown")
    tier = state.get("tier", "unknown")
    fallbacks = ", ".join(state.get("fallbacks", [])[:2])

    if status == "OK":
        print(f"API callable: main={main_route}, tier={tier}, fallbacks={fallbacks}")
    elif status == "DEGRADED":
        print(f"Main route degraded but callable: main={main_route}, fallbacks={fallbacks}")
    elif status == "LOCAL_FALLBACK":
        print("Local fallback is active.")
    else:
        print("No usable route detected.")


if __name__ == "__main__":
    main()
