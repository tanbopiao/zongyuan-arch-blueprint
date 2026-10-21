# Public Push Gate (Local + Remote)

This repository has a two-stage public push gate:

1. **Local pre-push**
   - `bash tools/prepush.sh`
   - Runs example validation, public safety scan, and ensures clean staged state.

2. **Remote gate**
   - `.github/workflows/public-safety.yml`
   - Runs on `push` to `main` and on `pull_request`.
   - Blocks public artifacts from carrying credential or private endpoint patterns.

## Usage

```bash
# Local pre-push
bash tools/prepush.sh

# Commit public-safe content
git commit -m "publish public artifact update"

# Push
git push

# Optional remote verification (after push)
python3 tools/verify_public_repo.py
```

## Remote Verification

`tools/verify_public_repo.py` checks:
- repository is public,
- required public files exist on `main`,
- public push docs reference the `prepush` gate.

This is used after pushing to confirm that the public artifact is actually visible.
