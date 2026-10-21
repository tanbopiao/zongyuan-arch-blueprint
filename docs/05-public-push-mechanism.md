# Public Push Mechanism

The push mechanism converts local derivative artifacts into stable public artifacts under a strict de-identification policy.

## Pipeline

```text
source baseline
  -> local derivative draft
  -> schema validation
  -> de-identification scan
  -> public commit
  -> public push
  -> remote verification
```

## Roles

- **Local workspace**: builds and verifies the derivative content.
- **Schema layer**: enforces stable public contracts.
- **Policy layer**: blocks credential leaks and unsafe public claims.
- **Remote registry**: hosts the public artifact for external use.

## Push Sequence

1. Prepare local content as a new independent derivative.
2. Validate schemas and examples.
3. Run the de-identification scanner.
4. Commit only public-safe files.
5. Push to the public repository.
6. Verify the public URL and public metadata.

## Safety Constraints

- Public pushes must not carry private tokens, keys, hostnames, or personal machine identifiers.
- Public claims must be neutral and traceable.
- If verification fails, the push is treated as incomplete, not successful.

## Recommended Local Checks

```bash
python3 tools/check_public_safety.py
python3 tools/validate_examples.py
git add -A
git commit -m "publish public artifact update"
git push
```

The two checks should be run before every public push.
