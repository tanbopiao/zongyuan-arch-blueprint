// Sanitized machine-readable shape for API router state.
export interface ApiRouterState {
  status: "OK" | "DEGRADED" | "LOCAL_FALLBACK" | "NO_ROUTE";
  choose: string;
  tier: string;
  capability: string;
  smoke_code: string;
  quota_hint: string;
  why: string;
  fallbacks: string[];
  local_reachable: boolean;
  local_fused: boolean;
  updated_at: string;
  source?: string;
  route_file_stale_seconds?: number;
}
