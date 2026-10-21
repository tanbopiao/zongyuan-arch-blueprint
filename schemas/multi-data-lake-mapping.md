# Multi-Data-Lake Mapping (De-identified)

This document describes how public derivatives can reference layered storage without exposing credentials.

## Layer Model

- L0 meta-constitution: immutable top-level rules.
- L1 kernel baseline: read-only foundation content.
- L2 truth store: append-only truth records.
- L3 boot memory: startup snapshot material.
- L4 business layer: dynamic, freely iterable application state.

## Public Mapping Pattern

```yaml
public_artifact:
  name: zongyuan-arch-blueprint
  source_of_truth: L2_public_contract
  storage_layers:
    - role: primary_showcase
      platform: public_git_host
      path: owner/repo-name
    - role: data_lake_mirror
      platform: object_storage
      path: models/example-owner/example-dataset
    - role: boot_seed
      platform: seed_repository
      path: seeds/zongyuan-root/boot
```

Rules:
- Public mappings reference `platform + path`, never credentials.
- Platform names may be generic (`public_git_host`, `object_storage`) if specific vendor names are unnecessary.
- Any vendor-specific endpoint, token, or private host is excluded from public artifacts.
- Public derivatives are read-only views; they never write back to baseline layers.
