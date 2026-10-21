# Federation Node Registration Contract

A public node registration request should use a public directory anchor, not raw credentials.

```json
{
  "schema": "zongyuan-arch-blueprint/node-registration@1.0",
  "did": "DID-BR-000002",
  "name": "blueprint-demo-node",
  "directory_anchor": {
    "version": "1.0.1",
    "tree_hash": "sanitized_tree_hash"
  },
  "capability": "read_only"
}
```

Required headers in a real deployment:

- `X-DID`
- `X-Directory-Tree-Version`
- `X-Directory-Tree-Hash`

Security notes:

- The public schema describes the shape, not live endpoint data.
- Actual tree hashes and DID values must come from the trusted source system.
- Public examples should replace live hashes with sanitized placeholders.
