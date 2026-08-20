from pydantic import BaseModel, Field


class RiskFactor(BaseModel):
    name: str
    score: float
    weight: float
    contribution: float


class AssetRiskResponse(BaseModel):
    asset_id: int
    hostname: str

    risk_score: float = Field(
        ge=0,
        le=100,
    )

    risk_level: str

    vulnerability_score: float = Field(
        ge=0,
        le=100,
    )

    incident_score: float = Field(
        ge=0,
        le=100,
    )

    asset_criticality_score: float = Field(
        ge=0,
        le=100,
    )

    risk_factors: list[RiskFactor]


class AssetRiskListResponse(BaseModel):
    total_assets: int
    assets: list[AssetRiskResponse]


class AlertPriorityResponse(BaseModel):
    alert_id: int
    asset_id: int
    title: str

    alert_severity: str
    alert_severity_score: float = Field(
        ge=0,
        le=100,
    )

    asset_risk_score: float = Field(
        ge=0,
        le=100,
    )

    priority_score: float = Field(
        ge=0,
        le=100,
    )

    priority: str
    recommendation: str
