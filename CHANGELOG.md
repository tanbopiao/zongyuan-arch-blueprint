# Changelog

## 1.2.0 - 2026-10-21

- Added GitHub Actions `public-safety` workflow.
- Added remote verification tool `tools/verify_public_repo.py`.
- Updated local pre-push gate docs to include local + remote stages.

## 1.1.0 - 2026-10-21

- Added public push mechanism docs.
- Added push policy, multi-data-lake mapping schema, and pre-push safety tooling.
- `tools/prepush.sh` now gates public pushes with local validation and de-identification scan.

## 1.0.0 - 2026-10-21

- Initial public architecture blueprint.
- L0-L4 governance, four-dimensional ontology, agent runtime, API router patterns, schemas, examples.
- Intentionally de-identified: no credentials, tokens, SSH keys, hostnames, private endpoints, or proprietary runtime secrets.
