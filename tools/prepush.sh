#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "==> validate examples"
python3 tools/validate_examples.py

echo "==> public safety scan"
python3 tools/check_public_safety.py

echo "==> git pre-push gate"
git add -A
git status --short

if ! git diff --quiet --cached; then
  echo "New public-safe content present. Commit first:"
  echo "  git commit -m \"Publish public push mechanism update\""
  exit 1
fi

echo "Pre-push gate passed. Push now with:"
echo "  git push"
