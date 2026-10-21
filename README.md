# ZONGYUAN-ROOT Arch Blueprint

**From ontology to self-governing agent architectures.**

ZONGYUAN-ROOT Arch Blueprint is a public derivative blueprint extracted from the ZONGYUAN-ROOT universal stable autonomous kernel. It focuses on the reusable high-level architecture patterns: a layered meta-kernel, four-dimensional ontology model, intent routing, truth convergence, low-consumption API routing, local fallback discipline, and self-healing circuit breakers.

This repository is intentionally **de-identified**. It does not contain private credentials, user tokens, SSH keys, hostnames, private endpoints, or proprietary runtime secrets.

## What This Repository Documents

- `docs/01-executive-summary.md` — one-page architecture value.
- `docs/02-architecture.md` — L0-L4 governance and the four-dimensional ontology.
- `docs/03-agent-runtime.md` — intent routing, local fallback, and steady-state execution.
- `docs/04-api-router.md` — low-consumption API router behavior and public contract.
- `schemas/` — machine-readable contracts for routing, truth reporting, and node registration.
- `examples/api-router-call-check.json` — sanitized sample output for the low-consumption keepalive workflow.

## Key Ideas

| Concept | Meaning |
|---|---|
| `Ω₀⊂⊙∞⊂Ω` | Source state, controllable evolution, and converged steady state. |
| L0-L4 | Absolute axioms, meta rules, intent routing, output standards, and self-healing. |
| Four-dimensional ontology | Space, time, property, and causality constraints. |
| Intent bifurcation | Separate baseline-asset operations from derivative extraction operations. |
| Low-consumption routing | Reuse recent probes, prefer free gateways, and fall back locally without burning quota. |
| Circuit breakers | Stop repeated failure loops, protect existing assets, and return to read-only mode. |

## Quick Start

Run the public push gate before pushing derivative content:

```bash
bash tools/prepush.sh
```

Reproduce the sanitized call-check sample:

```bash
python3 examples/reproduce_call_check.py
```

The sample uses the checked-in public output file. To inspect the machine-readable schema:

```bash
cat examples/api-router-call-check.json
```

## Repository Positioning

This is a **blueprint**, not a turnkey service. The value is the architecture: how a high-level agent should keep a single source of truth, separate baseline assets from derivatives, route API calls conservatively, and fail safely.

## License

MIT
