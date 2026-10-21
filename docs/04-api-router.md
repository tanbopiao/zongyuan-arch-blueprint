# Low-Consumption API Router

The API router keeps the agent capable of external model calls without burning quota on routine checks.

## Design Goals

- **Low cost**: routine keepalive reuses recent results instead of probing every provider.
- **Fast recovery**: external route degradation falls back to a local OpenAI-compatible service.
- **Observable state**: the router writes a compact JSON state file with the chosen route, tier, fallbacks, and last probe time.
- **Quota-safe refresh**: refreshes are time-windowed and provider cooldowns are respected.

## Call-Check State

A public router state file can use this shape:

```json
{
  "status": "OK",
  "choose": "kilo_free",
  "tier": "T1",
  "capability": "text",
  "smoke_code": "200",
  "quota_hint": "ok",
  "why": "Free gateway with sufficient anonymous rate limits.",
  "fallbacks": ["provider_b", "provider_c"],
  "local_reachable": true,
  "local_fused": false,
  "updated_at": "2026-10-21T00:00:00Z",
  "source": "api_router.call-check",
  "route_file_stale_seconds": 600
}
```

## Status Report Rule

Normal state should be reported in one line:

```text
API callable: main=choose, tier, fallbacks first 2
```

Expanded reporting is reserved for:

- `NO_ROUTE`: no usable external route.
- `LOCAL_FALLBACK`: local fallback is active.
- Severe degradation of the main route and fallbacks.
- Repeated degraded or no-route events.

## Refresh Policy

```text
if now - updated_at < freshness_window:
    reuse existing state
else:
    refresh lightweight probe
apply provider cooldown
choose lowest-cost acceptable route
```

The freshness window should be short enough to catch outages and long enough to avoid unnecessary API calls.

## Local Fallback Trigger

Local fallback is triggered only when:

- the chosen external route is unreachable, or
- the external route returns repeated failures, or
- quota is explicitly exhausted.

Local fallback should be a minimal OpenAI-compatible service. It is not used as a primary route when external providers are healthy.
