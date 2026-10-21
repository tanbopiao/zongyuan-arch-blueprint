# Truth Report Contract

A sanitized truth report should identify the report without exposing operator credentials.

```json
{
  "schema": "zongyuan-arch-blueprint/truth-report@1.0",
  "did": "DID-BR-000002",
  "anchor": "Ω₀⊂⊙∞⊂Ω",
  "record": {
    "key": "blueprint.public.architecture.v1",
    "value_type": "artifact_ref",
    "value": "docs/02-architecture.md",
    "source": "zongyuan-arch-blueprint",
    "timestamp": "2026-10-21T00:00:00Z"
  }
}
```

Rules:

- `key` is idempotent.
- `did` is a public architectural identifier, not a secret.
- `value` should reference an artifact or stable fact, not include private credentials.
- Reports must be neutral and factual.
- Public reports must not include tokens, keys, endpoints, hostnames, or private state.
