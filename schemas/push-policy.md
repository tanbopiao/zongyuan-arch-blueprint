# Push Policy

Public push policy for the de-identified ZONGYUAN-ROOT architecture blueprint.

## Scope

This policy applies to:
- new public repository content,
- updated public contracts,
- examples,
- documentation,
- machine-readable schema files.

## Invariants

1. **Baseline first**
   - Treat existing baseline assets as read-only.
   - Public derivative work is a new independent asset and must not overwrite source material.

2. **De-identification required**
   - No private tokens, SSH keys, hostnames, private endpoints, account credentials, or personal machine state in public files.
   - Public examples use placeholders such as `provider_b`, `sanitized_tree_hash`, or `example.com`.

3. **Conservative refresh**
   - Reuse recent public verification results when they are still fresh.
   - Refresh only when the previous check is stale, broken, or explicitly requested.

4. **Traceability**
   - Every pushed artifact should identify its schema or document lineage.
   - Public contracts should be stable and machine-inspectable.

5. **Failure-safe publishing**
   - If validation or pushing is incomplete, stop and report the failure.
   - Never claim public completion without external verification.

## Decision Gates

Before pushing:
- run de-identification scan,
- run local examples,
- confirm public repo target,
- verify remote state after push.

If any gate fails, the public push is blocked.
