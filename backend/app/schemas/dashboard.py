from pydantic import BaseModel


class AssetMetrics(BaseModel):
    total: int
    online: int
    offline: int


class ThreatMetrics(BaseModel):
    total: int


class VulnerabilityMetrics(BaseModel):
    total: int
    critical: int
    high: int


class IncidentMetrics(BaseModel):
    total: int
    open: int
    investigating: int
    resolved: int


class DashboardSummary(BaseModel):
    assets: AssetMetrics
    threats: ThreatMetrics
    vulnerabilities: VulnerabilityMetrics
    incidents: IncidentMetrics